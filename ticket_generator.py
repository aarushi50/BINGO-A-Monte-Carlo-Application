from random import choice, randint
import numpy as np


class BingoPlayer:
    """
    The instance of this class represents each player who participates in the game of Bingo. It has few attributes
    that describe the player.
    """

    def __init__(self, name, generated_ticket_array, ticket_type, money_paid):
        self.name = name
        self.generated_ticket_array = generated_ticket_array
        self.ticket_type = ticket_type
        self.money_paid = money_paid


class Ticket:
    """
    Each instance of this class is a ticket that a player buys to participate in the game. The generated ticket
    depends on the type of ticket that a player buys.
    NT = Normal Ticket
    ST = Special Ticket
    LT = Lucky Ticket
    """

    def __init__(self, ttype):
        self.ttype = ttype

        ticket = Ticket.basic_ticket()

        if self.ttype == 'NT':
            self.final_ticket = Ticket.normal_ticket(self,ticket)
        elif self.ttype == 'ST':
            self.final_ticket = Ticket.special_ticket(self,ticket)
        elif self.ttype == 'LT':
            self.final_ticket = Ticket.lucky_star_ticket(self,ticket)
        else:
            print("Enter a valid ticket type")
        print(self.final_ticket)


    # def __str__(self):
    #     return self.final_ticket

    def basic_ticket():

        # equate each column with initial ones place digit
        a_ticket = np.zeros([4, 9], dtype=np.dtype("U3"))
        a_ticket[0:3, 0] = 0  # better to write like this or in a loop
        a_ticket[0:3, 1] = 1
        a_ticket[0:3, 2] = 2
        a_ticket[0:3, 3] = 3
        a_ticket[0:3, 4] = 4
        a_ticket[0:3, 5] = 5
        a_ticket[0:3, 6] = 6
        a_ticket[0:3, 7] = 7
        a_ticket[0:3, 8] = 8
        a_ticket[3,0] = ''
        # select 4 random indexes of the ndarray in each row to equate them to ''
        index_row_0_list = [99]
        index_row_1_list = [99]
        index_row_2_list = [99]

        for i in range(0, 4, 1):
            status0 = True
            status1 = True
            status2 = True
            #   row 0
            index_row_0 = randint(0, 8)
            while status0:
                if index_row_0 in index_row_0_list:
                    index_row_0 = randint(0, 8)
                else:
                    status0 = False
                    index_row_0_list.append(index_row_0)
            a_ticket[0, index_row_0] = ''

            #   row 1
            index_row_1 = randint(0, 8)
            while status1:
                if index_row_1 in index_row_1_list:
                    index_row_1 = randint(0, 8)
                else:
                    status1 = False
                    index_row_1_list.append(index_row_1)
            a_ticket[1, index_row_1] = ''

            # row 2
            index_row_2 = randint(0, 8)
            while status2:
                if index_row_2 in index_row_2_list:
                    index_row_2 = randint(0, 8)
                else:
                    status2 = False
                    index_row_2_list.append(index_row_2)
            a_ticket[2, index_row_2] = ''

        # after equating 4 elements to '' in each row, select random numbers to generate the 5 numbers in each row
        for ii in range(0, 3, 1):
            for jj in range(0, 9, 1):
                duplicate = True
                if a_ticket[ii, jj] != '':
                    while duplicate:  # while loop is ensure no duplicates are selected in a ticket
                        z = str(randint(0, 9))
                        zz = a_ticket[ii, jj] + z
                        if zz not in a_ticket[0:3, jj]:
                            a_ticket[ii, jj] = zz
                            duplicate = False

                    if a_ticket[ii, jj] == '00':  # This condition replaces '00' with '10' since '00' is not valid
                        a_ticket[ii, jj] = '10'

        return a_ticket

    def normal_ticket(self, base_ticket):
        nticket = base_ticket
        nticket[3, 0] = 'NT'
        return nticket

    def special_ticket(self,base_ticket):
        sticket = base_ticket
        sticket[3, 0] = 'ST'
        return sticket

    def lucky_star_ticket(self, base_ticket):
        lticket_list = []
        lticket = base_ticket

        for x in range(0,3,1):  # ask if this loop can be avoided
            for y in range(0,9,1):
                if lticket[x,y] != '':
                    lticket_list.append(lticket[x,y])

        lucky_star_number = choice(lticket_list)
        lticket[3, 0] = 'LT'
        lticket[3, 1] = lucky_star_number
        return lticket


obj1 = Ticket('NT')
print("--------------------------------")
obj2 = Ticket('ST')
print("--------------------------------")
obj3 = Ticket('LT')
print("--------------------------------")

player1 = BingoPlayer('Jon', obj1, 'NT', 10)
print(player1.generated_ticket_array)

