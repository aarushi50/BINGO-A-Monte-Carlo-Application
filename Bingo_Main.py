import Bingo_Game as bg
import Bingo_Ticket as tg
from random import choice, randint
import pandas as pd


main_game_id_list = []
main_num_of_players_list = []
main_income_money_list =[]
main_payout_list =[]
main_lucky_star_wins_list = []
main_bingo_bonus_wins_list =[]
main_profit_list = []


def start_simulation():
    print(" ")
    print(" ******************************************Welcome to Bingo Simulation*********************************")
    print(" ")
    print("     >Tickets Price List:")
    print("         >>Normal - £10 \n         >>Special - £50 \n         >>Lucky Star - £100")
    print(" ")

    print("     >Winning Prizes:")
    print("         >>Four Corner - £30 \n         >>Single Line - £20 \n         >>Double Line - £20 \n         "
          ">>Full House - $50 \n")
    print(" ")
    print("             Buy Special Ticket And Get A Chance To Win BINGO BONUS of £100 ")
    print(" ")
    print("             Buy Lucky Star Ticket And Get A Chance To Win The JACKPOT of £200 ")
    print(" ")

    ngames = int(input("Enter the number of games for this round of simulation "))
    print("Number of games mentioned ",ngames)
    print(" ")
    each_game_details = input("Do you wish to print Brief / Detailed / No Summary? (B / D / N)")
    if each_game_details not in ('B', 'b', 'D', 'd', 'N', 'n'):
        print("Invalid input! Details will not be printed")
    print("Lets begin the simulation.....")
    print(" ")

    for count in range(1,ngames+1,1):
        print("                            >>>>>>>>>>Game Number: ", count, "<<<<<<<<<<< ")
        print("**************************************************************************************************** \n")
        nplayers = randint(1, 10)
        print("     >Number of players in this game ", nplayers, "\n" )
        ticket_dict = {}

        for i in range(1,nplayers+1, 1):
            ticket_type = choice(['NT', 'ST', 'LT'])
            player_ticket = tg.Ticket(ticket_type)
            ticket_dict.update({i: player_ticket.final_ticket_with_details})

        game = bg.BingoGame(ticket_dict) # list contains objects not list of arrays
        game.play_game()

        if each_game_details == 'B' or each_game_details == 'b':
            game.game_figures_brief()
        elif each_game_details == 'D' or each_game_details == 'd':
            game.game_figures_details()
        else:
            pass

        games_stats = game.return_values_for_stats()
        main_game_id_list.append(count)
        main_num_of_players_list.append(games_stats[0])
        main_income_money_list.append(games_stats[1])
        main_payout_list.append(games_stats[2])
        main_lucky_star_wins_list.append(games_stats[3])
        main_bingo_bonus_wins_list.append(games_stats[4])
        main_profit_list.append(games_stats[5])

        print("****************************************************************************************************")

    # print(main_game_id_list)
    # print(main_num_of_players_list)
    # print(main_income_money_list)
    # print(main_payout_list)
    # print(main_lucky_star_wins_list)
    # print(main_bingo_bonus_wins_list)
    # print(main_profit_list)
    #
    # print(len(main_game_id_list))
    # print(len(main_num_of_players_list))
    # print(len(main_income_money_list))
    # print(len(main_payout_list))
    # print(len(main_lucky_star_wins_list))
    # print(len(main_bingo_bonus_wins_list))
    # print(len(main_profit_list))


def simulation_summary_dataframe():
    # header1 = ['Game #', 'Number of players', 'Total Income',
    #            'Total Payout', '# of Lucky Star Winners',
    #            '# Bingo Bonus Winners', 'Total Profit']
    # simulation_summary_df = pd.DataFrame(main_game_id_list, main_num_of_players_list,main_income_money_list,
    #                                   main_payout_list, main_lucky_star_wins_list, main_bingo_bonus_wins_list,
    #                                   main_profit_list, columns=header1)

    # # simulation_summary_df.rename(index = 'Game #', columns = ['Game #','Number of players', 'Total Income',
    # #                                                           'Total Payout','# of Lucky Star Winners',
    # #

    # simulation_summary_df = pd.DataFrame([main_game_id_list, main_num_of_players_list],
    #                                      columns=['Game #','Number of players'])
    # simulation_summary_df['Total Income'] = main_income_money_list
    # simulation_summary_df['Total Payout'] = main_payout_list
    # simulation_summary_df['Lucky Winners'] = main_income_money_list
    # simulation_summary_df['Bingo Bonus Winners'] = main_bingo_bonus_wins_list
    # simulation_summary_df['Total Profit'] = main_profit_list

    print(simulation_summary_df)


start_simulation()
# simulation_summary_dataframe()

