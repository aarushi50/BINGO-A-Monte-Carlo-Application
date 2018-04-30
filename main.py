import bingo_game as bg
import ticket_generator as tg
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
    print(" ")
    print("Tickets Price List:")
    print("Normal - $10     |       Special - $50       |       Lucky Star - $100")
    print(" ")

    print("Winning Prizes:")
    print("Corner - $30        Single Line - $20       Double Line - $40       Full House - $50")
    print("Bingo Bonus  - $100                    Jackpot - $200")
    print(" ")
    print(" ")

    ngames = int(input("Enter the number of games for this round of simulation "))
    print("Number of games mentioned ",ngames)
    print(" ")
    print(" ")
    print("Lets begin the simulation.....")
    print(" ")

    for count in range(1,ngames+1,1):
        print(" >>>>>>>>>>Game Number: ", count, "<<<<<<<<<<<")
        nplayers = randint(1, 10)
        print("Number of players in this game ",nplayers )
        ticket_dict = {}

        for i in range(1,nplayers+1, 1):
            ticket_type = choice(['NT', 'ST', 'LT'])
            player_ticket = tg.Ticket(ticket_type)
            ticket_dict.update({i: player_ticket.final_ticket_with_details})

        game = bg.BingoGame(ticket_dict) # list contains objects not list of arrays
        game.play_game()
        game.game_figures_brief()
        games_stats = game.return_values_for_stats()
        main_game_id_list.append(count)
        main_num_of_players_list.append(games_stats[0])
        main_income_money_list.append(games_stats[1])
        main_payout_list.append(games_stats[2])
        main_lucky_star_wins_list.append(games_stats[3])
        main_bingo_bonus_wins_list.append(games_stats[4])
        main_profit_list.append(games_stats[5])

        print("***********************************************************************************************")

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


def summary_dataframe():
    # header = ['Game #', 'Number of players', 'Total Income',
    #            'Total Payout', '# of Lucky Star Winners',
    #            '# Bingo Bonus Winners', 'Total Profit']
    # simulation_summary_df = pd.DataFrame([main_game_id_list, main_num_of_players_list,main_income_money_list,
    #                                   main_payout_list, main_lucky_star_wins_list, main_bingo_bonus_wins_list,
    #                                   main_profit_list], columns=header)
    #
    # # simulation_summary_df.rename(index = 'Game #', columns = ['Game #','Number of players', 'Total Income',
    # #                                                           'Total Payout','# of Lucky Star Winners',
    # #

    simulation_summary_df = pd.DataFrame([main_game_id_list, main_num_of_players_list],
                                         columns=['Game #','Number of players'])
    simulation_summary_df['Total Income'] = main_income_money_list
    simulation_summary_df['Total Payout'] = main_payout_list
    simulation_summary_df['Lucky Winners'] = main_income_money_list
    simulation_summary_df['Bingo Bonus Winners'] = main_bingo_bonus_wins_list
    simulation_summary_df['Total Profit'] = main_profit_list

    print(simulation_summary_df)


start_simulation()
summary_dataframe()

