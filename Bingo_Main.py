import Bingo_Game as bg
import Bingo_Ticket as bt
from random import choice, randint
import pandas as pd
import matplotlib.pyplot as plt

"""
Instructions:
> Run the program
> Enter the number of size of simulation i.e. total number of Bingo games.
> Enter D / d if you wish to print detailed summary of each game
  OR Enter B / b if you wish to print brief summary of each game
  OR Enter N / n for not printing any summary (default).  
"""

# program variables
main_game_id_list = []
main_num_of_players_list = []
main_income_money_list = []
main_payout_list = []
main_bingo_bonus_wins_list = []
main_jackpot_wins_list = []
main_profit_list = []


def start_simulation()-> None:
    """
    This function initiates the simulation by prompting the user and calls other subsequent functions and
    creates objects of other classes.
    :return: None
    """
    print(" ")
    print(" ******************************************Welcome to Bingo Simulation*********************************")
    print(" ")
    print("     >Tickets Price List:")
    print("         >>Normal Ticket- £10 \n       >>Lucky Star Ticket - £15 \n       >>Special Ticket - £25")
    print(" ")

    print("     >Winning Prizes:")
    print("         >>Four Corners - £50 \n         >>Single Line - £40 \n         >>Double Line - £60 \n         "
          ">>Full House - $70 \n")
    print(" ")
    print("             Buy Lucky Star Ticket And Get A Chance To Win The BINGO BONUS of  £1000")
    print(" ")
    print("             Buy Special Ticket And Get A Chance To Win JACKPOT of £10,000 ")
    print(" ")

    ngames = int(input("Enter the number of games for this round of simulation "))
    print("Number of games entered ", ngames)
    print(" ")

    each_game_details = input("Do you wish to print Brief / Detailed / No Summary? (B / D / N)")
    if each_game_details not in ('B', 'b', 'D', 'd', 'N', 'n'):
        print("Invalid input! Details will not be printed")
    print("Lets begin the simulation.....")
    print(" ")

    for count in range(1, ngames+1, 1):
        print("                            >>>>>>>>>>Game Number: ", count, "<<<<<<<<<<< ")
        print("**************************************************************************************************** \n")
        nplayers = randint(10, 100)
        print("     >Number of players in this game ", nplayers, "\n" )

        # create bingo tickets and prepare the dictionary with necessary details
        ticket_dict = {}
        for i in range(1, nplayers+1, 1):
            ticket_type = choice(['NT', 'NT', 'NT', 'NT', 'ST', 'LT', 'LT', 'LT'])
            player_ticket = bt.BingoTicket(ticket_type)
            ticket_dict.update({i: player_ticket.final_ticket_with_details})

        # create Bingo Game instance
        game = bg.BingoGame(ticket_dict)
        game.play_game()

        # print detailed / brief / no summary
        if each_game_details == 'B' or each_game_details == 'b':
            game.game_figures_brief()
        elif each_game_details == 'D' or each_game_details == 'd':
            game.game_figures_details()
        else:
            pass

        # populate program variables for creating data frame in the next step
        games_stats = game.return_values_for_stats()
        main_game_id_list.append(count)
        main_num_of_players_list.append(games_stats[0])
        main_income_money_list.append(games_stats[1])
        main_payout_list.append(games_stats[2])
        main_bingo_bonus_wins_list.append(games_stats[3])
        main_jackpot_wins_list.append(games_stats[4])
        main_profit_list.append(games_stats[5])

        print("****************************************************************************************************")


def simulation_summary_dataframe()-> None:
    """
    This generates data frames using values stored during the simulating, prints statistical summary
    of the simulation and displays a plot.
    :return: None
    """

    sim_summary_df = pd.DataFrame({'Game #': main_game_id_list,
                                   'Number of players': main_num_of_players_list,
                                   'Total Income': main_income_money_list,
                                   'Total Payout': main_payout_list,
                                   'Bingo Bonus Winners': main_bingo_bonus_wins_list,
                                   'Jackpot Winners': main_jackpot_wins_list,
                                   'Total Profit': main_profit_list}, columns=['Game #',
                                                                               'Number of players',
                                                                               'Total Income',
                                                                               'Total Payout',
                                                                               'Bingo Bonus Winners',
                                                                               'Jackpot Winners',
                                                                               'Total Profit'])
    # setting the index
    sim_summary_df.set_index('Game #', inplace=True)
    # print(sim_summary_df.head(10))

    # display statistical summary
    print('\n')
    print('                             * * * Simulation Summary * * *                        ')
    print('------------------------------------------------------------------------------------------------')
    print(sim_summary_df.describe(), '\n')

    # calculate total and mean values for some Series in the data frame
    sim_total_bingo_bonus_wins = sim_summary_df['Bingo Bonus Winners'].sum()
    sim_jackpot_wins = sim_summary_df['Jackpot Winners'].sum()
    sim_total_profit = sim_summary_df['Total Profit'].sum()
    sim_mean_profit = sim_summary_df['Total Profit'].mean()
    sim_total_income = sim_summary_df['Total Income'].sum()
    sim_mean_income = sim_summary_df['Total Income'].mean()
    sim_total_payout = sim_summary_df['Total Payout'].sum()

    print("         > Total Bingo Bonus wins", sim_total_bingo_bonus_wins)
    print("         > Total Jackpot wins", sim_jackpot_wins)
    print("         > Total Profit", sim_total_profit)
    print("         > Mean Profit", sim_mean_profit)
    print("         > Total Income", sim_total_income)
    print("         > Mean Income", sim_mean_income)
    print("         > Total Payout", sim_total_payout)

    # creating the plot
    sim_df1 = sim_summary_df[['Total Income', 'Total Payout', 'Total Profit']]

    sim_df1.plot(use_index=True, loglog=True, legend=True, grid=True, figsize=(10, 10), marker='^').set(
         xlabel='Game #', ylabel='Dollars per game')
    plt.title('Simulation Financial Summary', fontsize=20)
    plt.show()


# call the main functions
start_simulation()
simulation_summary_dataframe()

# END
