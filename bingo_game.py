from random import *
import numpy as np

a1 = np.array([['2',    '12',   '',    '36',   '45',   '58',   '',    '',    '87'],
               ['',    '',    '',    '32',   '41',   '',    '',    '77',   '89'],
               ['9',    '13',   '22',   '',    '40',   '56',   '61',   '',    '81']], dtype=np.dtype("U3"))

a2 = np.array([['9',    '',    '25',   '39',   '',    '',    '',    '75',   '84'],
               ['8',    '',    '',    '31',   '47',   '',    '65',   '71',   ''],
               ['6',    '17',   '26',   '',    '',    '53',   '60',   '',    '']])

array_list = [a1]


class BingoGame:

    __winning_combination_status = [0,1,2,3] # 0 - corners, 1 - single line, 2 - double line, 4 - full house
    # __row_status = [False, False, False]
    # corner_status = False

    def __init__(self, card_list):  # money_per_game
        self.card_list = card_list  # card list is list of 2D ndarray
        #   self.money_per_game = money_per_game

    def play_game(self):

        lucky_number_list = []
        game_status = True
        corner_win = False
        # single_line_win = True
        full_house_win = False
        while game_status == True:
            lucky_number = str(randint(1,90))
            lucky_number_list.append(lucky_number)
            print(lucky_number)
            latest_array = BingoGame.strike_off_lnum(self, self.card_list[0], lucky_number)

            for i in range(0,len(self.card_list),1):
                if corner_win == False:
                    corner_win = BingoGame.four_corners(self, latest_array) # True/False is returned
                #
                # if not single_line_win:
                #     single_line_win = bingo_game.one_line_win(self, i,lucky_number) # True/False is returned
                # # double_line_win = two_line_win(i,lucky_number) - True/False is returned

                if not full_house_win:
                    full_house_win = BingoGame.house_win(self, latest_array) # True/False is returned

            if (corner_win == None and full_house_win) or (corner_win and full_house_win):
                game_status = False

        print("game status",game_status, "house win", full_house_win,"corner win", corner_win, "Game over!")

            # write logic to check game status to create exit condition
        # do money calculation
        # add code to store values for creating some results

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

    def one_line_win(self, b_array,lnum):

        func_row_status = [False, False, False]
        row_0 = list(b_array[0,0:9])
        row_1 = list(b_array[1,0:9])
        row_2 = list(b_array[2, 0:9])
        val = True

        if
        if func_row_status[0] == True or func_row_status[1] == True or func_row_status[2] == True:
            over_all_row_status = True
            print("Winner of Single Line is found!")
            return over_all_row_status

        else:

    def house_win(self, b_array):

        house_status = ""
        v = True
        #strike_off = False
        for i in range(0,3,1):
            for j in range(0,9,1):
                if (b_array[i,j] == '') or (b_array[i,j] == 'cut'):
                    pass
                else:
                    v = False
                    break

            if v == False:
                break

        # if v == False:
        #     for i in range(0, 3, 1):
        #         for j in range(0, 9, 1):
        #             z = a_array[i,j]
        #             if a_array[i, j] == lnum:
        #                 a_array[i, j] = ''
        #                 print("Number striked off", lnum)
        #                 strike_off = True
        #                 break
        #             else:
        #                 pass
        #         if strike_off:
        #             break

        house_status = v
        if house_status:
            print("Winner of house is found")
        return house_status


a = BingoGame(array_list)
a.play_game()

