from random import choice, randint
import numpy as np


def card_generator():

    card = np.zeros(shape=(3,9), dtype=np.dtype("U2"))
    print(card)

    t = 'True'
    num_min = 1
    num_max = 10
    for j in range(0, 9, 1):
        bingo_number_list = []
        for i in range(0, 3, 1):
                while t == 'True':
                    bingo_number = str(choice([randint(num_min, num_max), '']))
                    print("bingo_number selected", bingo_number)
                    if bingo_number == '':
                        break
                    else:
                        if bingo_number not in bingo_number_list:
                            card[i,j] = bingo_number
                            bingo_number_list.append(bingo_number)
                            print("bingo number in array",card[i,j])

                            break
                        else:
                            t = 'False'
        num_min += 10
        num_max += 10

    print("Generate card is:")
    print(card)
    return "Done"



print(card_generator())
#l = randint(0,10)
# for i in range(1,21,1):
#     r = choice([randint(1,10), 'space'])
#     print(r)