# BINGO - An application of Monte Carlo Simulation

## Team Member(s):
Aarushi Mishra

# Monte Carlo Simulation Scenario & Purpose:

A Bingo Club is planning to introduce two new windfalls to attract more participants. Windfall gain is any type of unusually high or abundant income that is sudden and/or unexpected.The profit perspective lies in the fact that it is highly uncertain whether a person will win the windfalls while the tickets for being eligible to win the windfalls cost higher than the usual tickets.

The aim of this simulation is to inform the decision of the club on what pay-out amount should be designated for each windfall gain so that club always earns some fair profit.

### About The Game

1. Every ticket has three rows and nine columns. The numbers on the ticket range from 1 to 90. There are total 15 numbers.
2. Types of ticket available: Normal Ticket - £ 10 , Lucky Star Ticket - £ 15 , Special Ticket - £ 25
3. Winning Combinations:
    a. Four Corners - £ 50 : All corner numbers are striked off <br />
    b. Single Line - £ 40 : All numbers in any one row are striked off <br />
    c. Double Line - £ 60 : All numbers any of the two rows are striked off <br />
    d. Full House - £ 70 : If all the numbers are striked off <br />

### Windfalls Being Introduced
The windfalls are actually a variation of Full House win.

1. Bingo Bonus
A Lucky Star ticket has a randomly selected lucky number associated with it. Every lucky star ticket has it's own lucky number. A   player who buys this ticket and wins Full House such that the last number he striked off was the lucky number, he wins a Bingo Bonus worth £1000.

2. Jackpot
A Special ticket is same as a normal ticket but with higher cst prize. A player who buys this ticket and wins Full HOuse such that the last number he striked off is the 100th number called by the caller, he wins the Jackpot worth £10,000.  


## Simulation's variables of uncertainty

The whole environment of the game can be divided into two parts. The varibales of uncertainty for those two parts are:

1. For ticket/card generation:

  a. Numbers printed on the ticket -> Uniform <br />
  b. Position of numbers on the ticket->  Uniform <br />
  c. Lucky number for lucky star ticket -> Uniform <br />

2. For Game:

  a. Number of players -> Discrete Random <br />
  b. The number called out by the caller -> Uniform <br />

## Assumptions and Limitations:

1. Each particiapnt buys only one ticket for a game.
2. Minimum number of players in one game is 10.
3. Maximum number of players in one game is 100.
4. No coinciding winning occurs.


## Hypothesis or hypotheses before running the simulation:

#### "The pay-out amount for each windfall must be double the price of the ticket." 

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

Initially, the price list was Normal Ticket - £ 10 , Lucky Star Ticket - £ 50 , Special Ticket - £ 100. According to the hypothesis, the payout for Bingo Bonus was £ 100 and for Jackpot it was £ 200. However, upon running the simulation for 1000 games, it was found that with these ticket prices and payout figures, club was making exceptionally huge profit. To adjust the profit fairly, I first adjusted the ticket prices and then the windfall payouts.

To conclude the simulation, the reuslts of the simulation provide enough evidence to reject the inital hypothesis. Therefore, the payout for each windfall should not be double the price of the ticket.

The Bingo Club can use the simulation results to decide the payout amount. A Bing Bonus of £1000 and Jackpot of £10,000 results in safe and fair mean profit for the club as well as the participants.


## Instructions on how to use the program:

1. Download Bingo_Main.py, Bingo_Ticket.py and Bingo_Game.py
2. Run Bingo_Main.py
3. Enter the size of simulation i.e. total number of Bingo games.
4. Enter D / d if you wish to print detailed summary of each game OR Enter B / b if you wish to print brief summary of each game
  OR Enter N / n for not printing any summary (default)
5. Hit Enter

## All Sources Used:

For exploring the topic and related aspects:

  https://en.wikipedia.org/wiki/Bingo_(United_Kingdom) <br />
  https://en.wikipedia.org/wiki/Bingo_(U.S.) <br />
  http://bingonut.net/windfall-gain-bingo.html <br />
  http://www.freebingoticket.com/tickets/10407 <br />
  https://www.statista.com/statistics/203432/bingo-gross-gaming-sales-in-the-uk/ <br />

For coding:

https://docs.python.org/3/ <br />
https://www.python.org/doc/ <br />
http://docs.python-guide.org/en/latest/writing/documentation/  <br />
https://docs.scipy.org/doc/numpy-1.14.0/reference/arrays.ndarray.html <br />
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html <br />
https://github.com/iSchool-590PR-2018Spring/in-class-examples/blob/master/week_11_Efficiency.ipynb <br />
"Programming in Python 3", 2nd Edition, by Mark Summerfield, ©2010

