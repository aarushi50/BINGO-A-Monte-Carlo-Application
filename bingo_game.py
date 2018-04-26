from random import *
import numpy as np

a1 = np.array([['2',    '12',   '',    '36',   '45',   '58',   '',    '',    '87'],
               ['',    '',    '',    '32',   '41',   '',    '',    '77',   '89'],
               ['9',    '13',   '22',   '',    '40',   '56',   '61',   '',    '81']], dtype=np.dtype("U3"))


array_list = [a1]


class BingoGame:
    """
    Each instance of this class represents a round of Bingo game. This class performs many functions such as
    determine the winner for each winning combination, if windfall gain occurs to a player, money calculations
    involved, etc.
    """

    __winning_combination_status = [0,1,2,3] # 0 - corners, 1 - single line, 2 - double line, 4 - full house
    # __row_status = [False, False, False]
    # corner_status = False

    def __init__(self, card_list):  # money_per_game
        self.card_list = card_list  # card list is list of 2D ndarray
        self.card_list2 = np.copy(card_list)
        #   self.money_per_game = money_per_game

    def play_game(self):

        lucky_number_list = []
        game_status = True
        corner_win = False
        single_line_win = False
        double_line_win = False
        full_house_win = False
        while game_status:
            lucky_number = str(randint(1,90))
            lucky_number_list.append(lucky_number)
            print(lucky_number)
            latest_array = BingoGame.strike_off_lnum(self, self.card_list[0], lucky_number)

            for i in range(0,len(self.card_list),1):
                if not corner_win:
                    corner_win = BingoGame.four_corners(self, latest_array) # True/False is returned

                if not single_line_win:
                    single_line_win = BingoGame.one_line_win(self, latest_array) # True/False is returned

                if not double_line_win:
                    double_line_win = BingoGame.two_line_win(self, latest_array)  #True/False is returned

                if not full_house_win:
                    full_house_win = BingoGame.house_win(self, latest_array) # True/False is returned

            if (corner_win == None and single_line_win and double_line_win and full_house_win ) or \
                    (corner_win and single_line_win and double_line_win and full_house_win):
                game_status = False

        called_numbers = set(lucky_number_list)
        print("GAME OVER!! \n")
        print("Game status :",game_status)
        print("House win :", full_house_win)
        print("Horner win :", corner_win)
        print("Single line win :", single_line_win)
        print("Double line win :", double_line_win)
        print("Numbers called : ", called_numbers)
        print("Ticket before game play: \n" )
        print(self.card_list2[0], "\n")
        print("Ticket after game play: \n")
        print(latest_array)

            # TODO : write logic to check game status to create exit condition
        # TODO:do money calculation
        # TODO: add code to store result values for creating some results

    def strike_off_lnum(self, a_array, lnum):

        for i in range(0, 3, 1):
            for j in range(0, 9, 1):
                if a_array[i, j] == lnum:
                    a_array[i, j] = 'cut'
                    break
                else:
                    pass
        return a_array

    def four_corners(self, b_array):

        if b_array[0][0] == '' or b_array[2][0] == '' or b_array[0][8] == '' or b_array[2][8] == '':
            corner_status = None
            print("Four corners not applicable")

        else:

            if b_array[0][0] == 'cut' and b_array[2][0] == 'cut' and b_array[0][8] == 'cut' and b_array[2][8] == 'cut':
                corner_status = True
                print(" Winner of Four Corners is found!")

            else:
                corner_status = False

        return corner_status

    def one_line_win(self, b_array):

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
            print("Single line winner found here!")
            return True
        else:
            return False

    def two_line_win(self, b_array):

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
            print("Double line winner found here!")
            return True
        else:
            return False

    def house_win(self, b_array):

        house_status = ""
        v = True

        for i in range(0,3,1):
            for j in range(0,9,1):
                if (b_array[i,j] == '') or (b_array[i,j] == 'cut'):
                    pass
                else:
                    v = False
                    break

            if v == False:
                break

        house_status = v
        if house_status:
            print("Winner of house is found")
        return house_status


a = BingoGame(array_list)
a.play_game()

