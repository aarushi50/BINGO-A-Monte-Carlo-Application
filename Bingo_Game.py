from random import randint
import numpy as np


class BingoGame:
    """
    Each instance of this class represents a round of Bingo game. Instance creation requires a dictionary to be
    passed as a parameter.

    Various methods of this class perform following main functions:
    1. Acts as the caller of the game ( calls out random numbers ) .
    2. Determine if a number must be striked off in a bingo ticket.
    3. Confirm and declare the winner of all possible winnings.
    4. Display game figures in brief.
    5. Display game figures in detail.
    6. Return important values for meaningful analysis and plotting.

    """

    def __init__(self, ticket_dict: dict):
        self.ticket_dict = ticket_dict
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
        self.bingo_bonus_wins = 0
        self.jackpot_wins = 0

        self.corner_winning_valid = BingoGame.check_if_corner_applicable(self)
        if not self.corner_winning_valid:
            print("         >>Four corners is not applicable for this round of game!")
            self.total_payout_pergame[0] = 0

    def play_game(self) -> None:
        """
        This method is the main method that starts the game. This method calls other methods to acomplish the
        functionality of the class. It creates and updates a number of variables that store all necessary
        information about the game. It takes self as the only parameter.

        :return: None
        """

        game_status = True          # value changes to True at the end of the game
        called_number_list = []
        called_number_count = 0
        latest_ticket_list = []
        corner_win = False          # value changes to True if winner is found
        single_line_win = False     # value changes to True if winner is found
        double_line_win = False     # value changes to True if winner is found
        full_house_win = False      # value changes to True if winner is found

        # calculate various figures that describe the game
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

        # game begins by calling random number between 1- 90
        while game_status:
            called_number = randint(1, 90)
            called_number_list.append(called_number)
            self.unique_numbers_called_list = set(called_number_list)
            self.called_number_count = self.called_number_count + 1     # for checking if a player wins the Jackpot

            # loop to strike off a number if matched with the called number , each time
            # if a number in the ticket array matches the called number, its sign is changed to negative
            for i in range(0, len(self.ticket_dict), 1):
                latest_ticket_list[i] = BingoGame.strike_off_lnum(self, self.ticket_dict[i+1][0], called_number)

            for i in range(0, len(latest_ticket_list), 1):

                # determine winner of four corners
                if self.corner_winning_valid:   # look for corner winner only if corner win applicable
                    if not corner_win:
                        corner_win = BingoGame.four_corners(self, latest_ticket_list[i], corner_win, i+1)
                else:
                    corner_win = True

                # determine winner of single line
                if not single_line_win:
                    single_line_win = BingoGame.one_line_win(self, latest_ticket_list[i], i+1)

                # determine winner of double line
                if not double_line_win:
                    double_line_win = BingoGame.two_line_win(self, latest_ticket_list[i], i+1)

                # determine winner of full house / full house with Bingo Bonus / full hour with Jackpot
                if not full_house_win:
                    full_house_win = BingoGame.house_win(self, i+1, latest_ticket_list[i], self.ticket_dict[i+1][1],
                                                         self.ticket_dict[i+1][2], called_number, called_number_count)

            # determine if all winners are found and finish the game
            if corner_win and single_line_win and double_line_win and full_house_win:
                game_status = False
                self.total_profit = self.total_received_money - sum(self.total_payout_pergame)

        self.unique_numbers_called_list = set(called_number_list)
        # print("main", self.unique_numbers_called_list)
        print("\n          !! GAME COMPLETE !!")

    def strike_off_lnum(self, a_array: np.ndarray, cnum: int) -> np.ndarray:
        """
        This number visits every ticket in the dictionary, passed while instance creation, to see if any number
        matches the called number. If a match is found, the sign of the matched number is changed to negative.

        :param a_array: np.ndarray
        :param cnum: int
        :return: np.ndarray
        """

        for i in range(0, 3, 1):
            for j in range(0, 9, 1):
                if a_array[i, j] == cnum:
                    a_array[i, j] = a_array[i, j] * -1
                    # print(a_array)
                    break
                else:
                    pass
        # print(a_array)
        return a_array

    def check_if_corner_applicable(self) -> bool:
        """
        This function checks if four corners winning is even applicable for the game. It returns True if there is
        even one ticket with all four corners as numbers and not 0. It return False if there is not even one ticket
        with all four corners as numbers.

        :return: bool
        """
        var = False
        for i in range(1, len(self.ticket_dict) + 1, 1):
            arr = self.ticket_dict[i][0]
            if arr[0, 0] == 0 or arr[2,0] == 0 or arr[0, 8] == 0 or arr[2, 8] == 0:
                pass
            else:
                var = True  # at least one ticket with 4 corners is present
                break

        return var

    def four_corners(self, b_array: np.ndarray, prev_corner_status: bool, ticket_id: int) -> bool:
        """

        :param b_array: np.ndarray
        :param prev_corner_status: bool
        :param ticket_id: int
        :return: bool
        """

        if prev_corner_status:  # check if four corner winner is already found
                corner_status = True
        else:
            if b_array[0][0] < 0 and b_array[2][0] < 0 and b_array[0][8] < 0 and b_array[2][8] < 0:

                if (b_array[0, 0] * -1 in self.unique_numbers_called_list) and \
                        (b_array[2, 0] * -1 in self.unique_numbers_called_list) and \
                        (b_array[0, 8] * -1 in self.unique_numbers_called_list) and \
                        (b_array[2, 8] * -1 in self.unique_numbers_called_list):
                    check_win = True
                else:
                    check_win = False

                if check_win:               # confirm if all the numbers striked off were called
                    corner_status = True
                    print("         >>Winner of Four Corners is found!")
                    self.total_payout_pergame[0] = 50
                    self.winners['Corner'].append(ticket_id)
                else:
                    corner_status = False
                    self.total_payout_pergame[0] = 0
                    print("You are not winner yet! Proceeding to next call")
            else:
                corner_status = False
                self.total_payout_pergame[0] = 0

        return corner_status

    def one_line_win(self, b_array: np.ndarray, ticket_id: int) -> bool:
        """

        :param b_array:
        :param ticket_id:
        :return:
        """

        func_row_status = [True, True, True]  # status corresponds to each row
        row_0 = list(b_array[0, 0:9])
        row_1 = list(b_array[1, 0:9])
        row_2 = list(b_array[2, 0:9])

        for i in range(0, 9, 1):
            if row_0[i] <= 0:
                pass
            else:
                func_row_status[0] = False  # status changes to False if even number is non-negative(not called yet)

            if row_1[i] <= 0:
                pass
            else:
                func_row_status[1] = False

            if row_2[i] <= 0:
                pass
            else:
                func_row_status[2] = False

        # if status of any row is ultimately True
        if any(func_row_status):
            all_num_striked_off = True
            check_row_list = 0
            if func_row_status[0]:
                check_row_list = row_0
            elif func_row_status[1]:
                check_row_list = row_1
            elif func_row_status[2]:
                check_row_list = row_2
            else:
                pass

            # confirm if all numbers, in row whose status is noe True, striked off were called
            for i in range(0, len(check_row_list), 1):
                if check_row_list[i] < 0:
                    if check_row_list[i] * -1 in self.unique_numbers_called_list:
                        pass
                    else:
                        all_num_striked_off = False
                else:
                    pass

            if all_num_striked_off:
                self.winners['Single Line'].append(ticket_id)
                self.total_payout_pergame.append(45)
                print("         >>Single line winner found!")
                return True
        else:
            return False

    def two_line_win(self, b_array: np.ndarray, ticket_id: int) -> bool:
        """

        :param b_array:
        :param ticket_id:
        :return:
        """

        check_for_striked_num = False
        func_row_status = [True, True, True]    # status corresponds to each row
        row_0 = list(b_array[0, 0:9])
        row_1 = list(b_array[1, 0:9])
        row_2 = list(b_array[2, 0:9])

        for i in range(0, 9, 1):
            if row_0[i] <= 0:
                pass
            else:
                func_row_status[0] = False  # status changes to False if even number is non-negative(not called yet)

            if row_1[i] <= 0:
                pass
            else:
                func_row_status[1] = False

            if row_2[i] <= 0:
                pass
            else:
                func_row_status[2] = False

        # check which two row's status has changed to True
        if func_row_status[0] and func_row_status[1]:
            check_row_list = row_0 + row_1
            check_for_striked_num = True    # set value to True to confirm the win in the next step
        elif func_row_status[0] and func_row_status[2]:
            check_row_list = row_0 + row_2
            check_for_striked_num = True
        elif func_row_status[1] and func_row_status[2]:
            check_row_list = row_1 + row_2
            check_for_striked_num = True
        else:
            check_row_list = 0

        # confirm if all the numbers striked off in the two rows were called
        if check_for_striked_num:
            all_num_striked_off = True
            for i in range(0, len(check_row_list),1):
                if check_row_list[i] < 0:
                    if check_row_list[i] * -1 in self.unique_numbers_called_list:
                        pass
                    else:
                        all_num_striked_off = False

            if all_num_striked_off:
                self.winners['Double Line'].append(ticket_id)
                self.total_payout_pergame.append(65)
                print("         >>Double line winner found!")
                return True
            else:
                return False
        else:
            return False

    def house_win(self, ticket_id: int, b_array: np.ndarray, ticket_type: str, lucky_star_num: int,
                  called_num: int, called_num_count: int) -> bool:

        house_status = True         # status of full house win

        # check if full house winner already found
        for i in range(0, 3, 1):
            for j in range(0, 9, 1):
                if b_array[i, j] <= 0:
                    pass
                else:
                    house_status = False    # status changes to False if any of the number is non - negative
                    break

            if not house_status:
                break

        if house_status:
            # check if all numbers striked off were called
            all_num_striked_off = True

            for i in range(0, 3, 1):
                for j in range(0, 9, 1):
                    if b_array[i, j] < 0:
                        if b_array[i, j] * -1 in self.unique_numbers_called_list:
                            pass
                        else:
                            all_num_striked_off = False
                            break
                    else:
                        pass

                if not all_num_striked_off:
                    break

            # if numbers confirmed, determine if full house / full house with Bingo Bonus / full house with Jackpot
            if all_num_striked_off:
                self.winners['Full House'].append(ticket_id)

                # full house with Bingo Bonus
                if ticket_type == 'LT':
                    if called_num == lucky_star_num:
                        self.bingo_bonus_wins = self.bingo_bonus_wins + 1
                        self.total_payout_pergame.append(1000)
                        print("         >>Congratulations!! You win full house Bingo Bonus! You are the Lucky Star!!")

                    else:
                        print("         >>Winner of full house found! Hard Luck - No Bingo Bonus this time")
                        self.total_payout_pergame.append(70)

                # full house with Jackpot
                elif ticket_type == 'ST':
                    if called_num_count == 100:  # check if last number striked off is the 100th number called
                        self.jackpot_wins = self.jackpot_wins + 1
                        self.total_payout_pergame.append(10000)
                        print("         >>Congratulations!! You win full house with Jackpot! You are Special!!")
                    else:
                        print("         >>Winner of full house found! Hard Luck - No Jackpot this time")
                        self.total_payout_pergame.append(70)

                # full house only
                else:
                    self.total_payout_pergame.append(70)
                    print("         >>Winner of normal ticket full house found!")

        else:
            house_status = False
        return house_status

    def game_figures_brief(self) -> None:
        """
        This function prints only some figures of the game when user enter B or b upon being
        prompted, initially.
        :return: None
        """

        print("                                 *******Brief Game Summary******* \n")
        print("     > Total tickets sold:", self.total_tickets_sold)
        print("     > Total money received: £", self.total_received_money)
        print("     > Total payout: £", sum(self.total_payout_pergame))
        print("     > Total profit: £", self.total_profit)
        print("     > Bingo bonus wins:", self.bingo_bonus_wins)
        print("     > Jackpot wins:", self.jackpot_wins,"\n")

    def game_figures_details(self) -> None:
        """
        This function prints all figures of the game when user enter D or d upon being
        prompted, initially.

        :return: None
        """

        print("                                 *******Detailed Game Summary******* \n")
        print("     > Numbers called : {}".format(self.unique_numbers_called_list))
        print("     > Total number of calls:", self.called_number_count)
        print("     > Winner IDs:")
        for k, v in self.winners.items():
            print("         >>", k, "Winner is Player ID {}".format(v))
        print("     > Bingo bonus wins:", self.bingo_bonus_wins)
        print("     > Jackpot wins:", self.jackpot_wins, "\n")
        print("     > Tickets sold summary:")
        print("         >> Normal tickets sold:", self.total_normal_tickets)
        print("         >> Lucky Star tickets sold:", self.total_lucky_star_tickets)
        print("         >> Special tickets sold:", self.total_special_tickets)
        print("         >> Total tickets sold:", self.total_tickets_sold, "\n")
        print("     > Financial Summary:")
        print("         >> Total money received: £", self.total_received_money)
        print("         >> Total payout: £", sum(self.total_payout_pergame))
        print("         >> Total profit: £", self.total_profit, "\n \n")

    def return_values_for_stats(self) -> tuple:
        """
        This function returns a tuple that consists of following values in sequence:
        1. length of the ticket dictionary ( indicates number of players in the game).
        2. Total money received.
        3. Total pay-outs made at the end of the game.
        4. Total Bingo Bous winners in the game.
        5. Total Jackpot winners in the game.

        :return: tuple
        """
        return len(self.ticket_dict), self.total_received_money, sum(self.total_payout_pergame),\
            self.bingo_bonus_wins, self.jackpot_wins, self.total_profit


# Run this code to see the functionality of class for a sample ticket, separately
#
# a1 = np.array([[10,  0,  0, 38, 41, 56, 66,  0,  0],
#               [8,  0, 23, 40,  0,  0, 64,  0, 82],
#               [7,  0, 25, 36,  0, 52,  0, 71,  0]], dtype=int)
#
# temp_dict = {1: (a1, 'NT', '', 10)}
#
# a = BingoGame(temp_dict)
# a.play_game()
# print("---------------------------------------------------------------------------------------------------")
# a.game_figures_brief()
# a.game_figures_details()
