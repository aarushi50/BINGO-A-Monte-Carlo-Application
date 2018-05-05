from random import choice, randint
import numpy as np


class BingoTicket:
    """
    Each instance of this class is a ticket that a player buys to participate in the game. The ticket is generated
    according to the type of ticket that a player buys.
    NT = Normal Ticket (£ 10)
    LT = Lucky Star Ticket (£ 15)
    ST = Special Ticket (£ 25)
    """

    def __init__(self, ttype):

        self.ttype = ttype

        # create a general ticket
        general_ticket = BingoTicket.basic_ticket(self)

        # generate specific type of ticket using previously generated general ticket
        if self.ttype == 'NT':
            self.final_ticket_with_details = BingoTicket.normal_ticket(self, general_ticket)
        elif self.ttype == 'ST':
            self.final_ticket_with_details = BingoTicket.special_ticket(self, general_ticket)
        elif self.ttype == 'LT':
            self.final_ticket_with_details = BingoTicket.lucky_star_ticket(self, general_ticket)
        else:
            print("Enter a valid ticket type")

    def __str__(self):

        return '{} \n Type = {} \n Cost = £{} '.format(self.final_ticket_with_details[0],
                                                       self.final_ticket_with_details[1],
                                                       self.final_ticket_with_details[3])

    def basic_ticket(self) -> np.ndarray: # specify return type
        """
        This method creates a basic ticket in three steps:
        1. Create ndarray with 3 rows and 9 columns.
        2. In each row, randomly equate 4 elements of the ndarray to 0 (0 refers to blank)
        3. Randomly assign a number to the remaining 15 places in the ndarray

        The final tickets consists of 15 randomly chosen numbers ranging from 1 - 90.

        :return: ndarray
        """

        # Step 1
        a_ticket = np.zeros([3, 9], dtype=int)
        a_ticket[0:3, 0] = 9  # better to write like this or in a loop
        a_ticket[0:3, 1] = 1
        a_ticket[0:3, 2] = 2
        a_ticket[0:3, 3] = 3
        a_ticket[0:3, 4] = 4
        a_ticket[0:3, 5] = 5
        a_ticket[0:3, 6] = 6
        a_ticket[0:3, 7] = 7
        a_ticket[0:3, 8] = 8

        # Step 2
        index_row_0_list = []
        index_row_1_list = []
        index_row_2_list = []

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
            a_ticket[0, index_row_0] = 0

            #   row 1
            index_row_1 = randint(0, 8)
            while status1:
                if index_row_1 in index_row_1_list:
                    index_row_1 = randint(0, 8)
                else:
                    status1 = False
                    index_row_1_list.append(index_row_1)
            a_ticket[1, index_row_1] = 0

            # row 2
            index_row_2 = randint(0, 8)
            while status2:
                if index_row_2 in index_row_2_list:
                    index_row_2 = randint(0, 8)
                else:
                    status2 = False
                    index_row_2_list.append(index_row_2)
            a_ticket[2, index_row_2] = 0

        # Step 3
        for ii in range(0, 3, 1):
            for jj in range(0, 9, 1):
                duplicate = True
                if a_ticket[ii, jj] != 0:
                    while duplicate:  # while loop is ensure no duplicate numbers are selected in a ticket
                        z = randint(1, 10)
                        if a_ticket[ii, jj] == 9:
                            zz = (a_ticket[ii, jj] * 0) + z
                        else:
                            zz = (a_ticket[ii, jj] * 10) + z
                        if zz not in a_ticket[0:3, jj]:
                            a_ticket[ii, jj] = zz
                            duplicate = False

        return a_ticket

    def normal_ticket(self, base_ticket: np.ndarray) -> tuple:
        """
        This method returns a ticket whose type is normal along with other details.
        It returns a tuple of size 4 whose elements are at ticket, type of ticket, lucky number(if any, 0 otherwise)
        and cost, in sequence ( sequence is important to note).

        :param base_ticket:
        :return: tuple
        """

        return base_ticket, self.ttype, 0, 10

    def lucky_star_ticket(self, base_ticket:np.ndarray) -> tuple:
        """
        This method returns a ticket whose type is lucky star along with other details.
        It returns a tuple of size 4 whose elements are at ticket, type of ticket, lucky number
        and cost, in sequence ( sequence is important to note).
        It randomly selects a lucky star number for each ticket before returning the ticket.
        :param base_ticket:
        :return: tuple
        """
        lticket_list = []
        lticket = base_ticket

        for x in range(0, 3, 1):
            for y in range(0, 9, 1):
                if lticket[x,y] != 0:
                    lticket_list.append(lticket[x, y])

        lucky_star_number = choice(lticket_list)    # choose lucky star number
        return lticket, self.ttype, lucky_star_number, 15

    def special_ticket(self, base_ticket: np.ndarray) -> tuple:
        """
        This method returns a ticket whose type is special along with other details.
        It returns a tuple of size 4 whose elements are ticket array, type of ticket, lucky number(if any, 0 otherwise)
        and cost, in sequence ( sequence is important to note).
        :param base_ticket:
        :return: tuple
        """

        return base_ticket, self.ttype, 0, 25


# Run this to see the generated ticket separately
# obj1 = BingoTicket('NT')
# print(obj1)
# print("--------------------------------")
#
# obj2 = BingoTicket('LT')
# print(obj1)
# print("--------------------------------")
#
# obj3 = BingoTicket('ST')
# print(obj1)
# print("--------------------------------")
