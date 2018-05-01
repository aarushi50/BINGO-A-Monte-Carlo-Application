from random import *

# ab = np.array([['',    '12',   '',    '36',   '45',   '58',   '',    '',    '87'],
#                ['3',    '',    '',    '',   '41',   '',    '',    '77',   ''],
#                ['4',    '13',   '22',   '',    '40',   '56',   '61',   '',    '88']], dtype=np.dtype("U3"))
#
#
# a1 = np.array([['',    '11',   '',    '36',   '',   '58',   '',    '',    '87'],
#                ['1',    '12',    '',    '38',   '41',   '',    '',    '77',   '89'],
#                ['',    '13',   '22',   '',    '40',   '56',   '61',   '',    '']],dtype=np.dtype("U3"))
#
#
# t_dict = {1: (ab, 'NT', '', 10), 2: (a1, 'LT', '', 100)}


class BingoGame:
    """
    Each instance of this class represents a round of Bingo game. This class performs many functions such as
    determine the winner for each winning combination, if windfall gain occurs to a player, money calculations
    involved, etc.
    """

    def __init__(self, ticket_dict):
        self.ticket_dict = ticket_dict  # card list is list of 2D ndarray
        self.total_tickets_sold = 0
        self.total_normal_tickets = 0
        self.total_special_tickets = 0
        self.total_lucky_star_tickets = 0
        self.called_number_count = 0
        self.unique_numbers_called_list = []
        self.total_received_money = 0
        self.total_payout_pergame = [0]
        self.total_profit = 0
        self.winners = {'Corner': [], 'Single Line': [], 'Double Line': [], 'Full House': []}
        self.lucky_star_wins = 0
        self.bingo_bonus_wins = 0

    def play_game(self):

        game_status = True
        called_number_list = []
        called_number_count = 0
        latest_ticket_list = []
        corner_win = False
        single_line_win = False
        double_line_win = False
        full_house_win = False
        for i in range(0, len(self.ticket_dict), 1):
            latest_ticket_list.append(self.ticket_dict[i+1][0])
            self.total_tickets_sold += +1

            if self.ticket_dict[i+1][1] == 'NT':
                self.total_normal_tickets += 1
            elif self.ticket_dict[i + 1][1] == 'ST':
                self.total_special_tickets += 1
            else:
                self.total_lucky_star_tickets += 1

            self.total_received_money += self.ticket_dict[i+1][3]

        while game_status:
            called_number = str(randint(1,90))
            called_number_list.append(called_number)
            self.called_number_count = self.called_number_count + 1     # for Bingo Bonus
            # print(lucky_number)

            for i in range(0,len(self.ticket_dict),1):
                latest_ticket_list[i] = BingoGame.strike_off_lnum(self, self.ticket_dict[i+1][0], called_number)

            for i in range(0, len(latest_ticket_list),1):

                if corner_win == False:
                    corner_win = BingoGame.four_corners(self, latest_ticket_list[i], corner_win, i+1)

                if not single_line_win:
                    single_line_win = BingoGame.one_line_win(self, latest_ticket_list[i], i+1)

                if not double_line_win:
                    double_line_win = BingoGame.two_line_win(self, latest_ticket_list[i], i+1)

                if full_house_win == False:
                    full_house_win = BingoGame.house_win(self, i+1, latest_ticket_list[i], self.ticket_dict[i+1][1],
                                                         self.ticket_dict[i+1][2],called_number, called_number_count)

            if (corner_win == None and single_line_win and double_line_win and full_house_win ) or \
                    (corner_win and single_line_win and double_line_win and full_house_win):

                game_status = False

        self.unique_numbers_called_list = set(called_number_list)
        print("\n          !! GAME COMPLETE !!")

    def strike_off_lnum(self, a_array, lnum):

        for i in range(0, 3, 1):
            for j in range(0, 9, 1):
                if a_array[i, j] == lnum:
                    a_array[i, j] = 'cut'
                    break
                else:
                    pass
        return a_array

    def four_corners(self, b_array, corner_check, ticket_Id):

        # print("first visit corner")
        if corner_check == None or corner_check == True:
            corner_status = True
            self.winners['Corner'].append(ticket_Id)

        else:
            if b_array[0][0] == '' or b_array[2][0] == '' or b_array[0][8] == '' or b_array[2][8] == '':
                corner_status = None

                print("         >>Four corners is not applicable")
                self.total_payout_pergame[0] = 0

            elif b_array[0][0] == 'cut' and b_array[2][0] == 'cut' and b_array[0][8] == 'cut' and b_array[2][8] == 'cut':
                corner_status = True
                print("         >>Winner of Four Corners is found!")
                self.total_payout_pergame[0] = 30
            else:
                corner_status = False
                self.total_payout_pergame[0] = 0

        return corner_status

    def one_line_win(self, b_array,ticket_Id ):

        # print("first visit single line")
        func_row_status = [True, True, True]
        row_0 = list(b_array[0, 0:9])
        row_1 = list(b_array[1, 0:9])
        row_2 = list(b_array[2, 0:9])

        for i in range(0,9,1):
            if row_0[i] == '' or row_0[i] == 'cut':
                pass
            else:
                func_row_status[0] = False

            if row_1[i] == '' or row_1[i] == 'cut':
                pass
            else:
                func_row_status[1] = False

            if row_2[i] == '' or row_2[i] == 'cut':
                pass
            else:
                func_row_status[2] = False

        if any(func_row_status):
            self.winners['Single Line'].append(ticket_Id)
            self.total_payout_pergame.append(20)
            print("         >>Single line winner found!")
            return True
        else:
            return False

    def two_line_win(self, b_array, ticket_Id):

        # print("first visit double line")
        func_row_status = [True, True, True]
        row_0 = list(b_array[0, 0:9])
        row_1 = list(b_array[1, 0:9])
        row_2 = list(b_array[2, 0:9])

        for i in range(0, 9, 1):
            if row_0[i] == '' or row_0[i] == 'cut':
                pass
            else:
                func_row_status[0] = False

            if row_1[i] == '' or row_1[i] == 'cut':
                pass
            else:
                func_row_status[1] = False

            if row_2[i] == '' or row_2[i] == 'cut':
                pass
            else:
                func_row_status[2] = False

        if ((func_row_status[0] == True and func_row_status[1]) or (func_row_status[0] == True and func_row_status[2])
                or (func_row_status[1] == True and func_row_status[2])):
            self.winners['Double Line'].append(ticket_Id)
            self.total_payout_pergame.append(40)
            print("         >>Double line winner found!")
            return True
        else:
            return False

    def house_win(self,ticket_Id, b_array, ticket_type, lucky_star_num, called_num, called_num_count):

        house_status = True
        for i in range(0, 3, 1):
            for j in range(0, 9, 1):
                if (b_array[i, j] == '') or (b_array[i, j] == 'cut'):
                    pass
                else:
                    house_status = False
                    break

            if house_status == False:
                break

        if house_status:
            self.winners['Full House'].append(ticket_Id)
            if ticket_type == 'LT':
                if called_num == lucky_star_num:
                    self.lucky_star_wins = self.lucky_star_wins + 1
                    self.total_payout_pergame.append(200)
                    print("         >>Congratulations!! You win full house with Jackpot! You are the Lucky Star!!")

                else:
                    print("         >>Winner of full house found! Hard Luck - No Jackpot this time")
                    self.total_payout_pergame.append(50)
            elif ticket_type == 'ST':
                if called_num_count == 150:
                    self.bingo_bonus_wins = self.bingo_bonus_wins + 1
                    self.total_payout_pergame.append(100)
                    print("         >>Congratulations!! You win full house with Bingo Bonus! You are Special!!")
                else:
                    print("         >>Winner of full house found! Hard Luck - No Bingo Bonus this time")
                    self.total_payout_pergame.append(50)

            else:
                self.total_payout_pergame.append(50)
                print("         >>Winner of normal ticket full house found!")

        return house_status

    def game_figures_brief(self):
        self.total_profit = self.total_received_money - sum(self.total_payout_pergame)
        print("                                 *******Brief Game Summary******* \n")
        print("     > Total tickets sold:", self.total_tickets_sold)
        print("     > Total money received: £", self.total_received_money)
        print("     > Total payout: £", sum(self.total_payout_pergame))
        print("     > Total profit: £", self.total_profit)
        print("     > Lucky Star wins:", self.lucky_star_wins)
        print("     > Bingo Bonus wins:", self.bingo_bonus_wins,"\n")

    def game_figures_details(self):

        self.total_profit = self.total_received_money - sum(self.total_payout_pergame)
        print("                                 *******Detailed Game Summary******* \n")
        print("     > Numbers called : ", self.unique_numbers_called_list)
        print("     > Total number of calls:", self.called_number_count)
        print("     > Winner IDs:")
        for k, v in self.winners.items():
            print("         >>",k,"Winner is Player ID", v)
        print("     > Lucky Star wins:", self.lucky_star_wins)
        print("     > Bingo Bonus wins:", self.bingo_bonus_wins,"\n")
        print("     > Tickets sold summary:")
        print("         >> Normal tickets sold:", self.total_normal_tickets)
        print("         >> Special tickets sold:", self.total_special_tickets)
        print("         >> Lucky Star tickets sold:", self.total_lucky_star_tickets)
        print("         >> Total tickets sold:", self.total_tickets_sold,"\n")
        print("     > Financial Summary:")
        print("         >> Total money received: £", self.total_received_money)
        print("         >> Total payout: £", sum(self.total_payout_pergame))
        print("         >> Total profit: £", self.total_profit, "\n \n")

    def return_values_for_stats(self):
        return len(self.ticket_dict), self.total_received_money, sum(self.total_payout_pergame), self.lucky_star_wins, \
               self.bingo_bonus_wins, self.total_profit
#
#
# a = BingoGame(t_dict)
# a.play_game()
# # print("---------------------------------------------------------------------------------------------------")
# a.game_figures_brief()
# a.game_figures_details()
#
