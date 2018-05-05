# BINGO - An application of Monte Carlo Simulation

## Team Member(s):
Aarushi Mishra

# Monte Carlo Simulation Scenario & Purpose:

A Bingo Club is planning to introduce two new windfalls to attract more participants. Windfall gain is any type of unusually high or abundant income that is sudden and/or unexpected.The profit perspective lies in the fact that it is highly uncertain whether a person will win the windfalls while the tickets for being eligible to win the windfalls cost higher than the usual tickets.

The aim of this simulation is to inform the decision of the club on what pay-out amount should be designated for each windfall gain so that club always earns some fair profit.

## About The Game
1. Types of ticket available: Normal Ticket - £ 10 , Lucky Star Ticket - £ 15 , Special Ticket - £ 25
2. Winning Combinations:
    a. Four Corners - £ 50 : All corner numbers are striked off <br />
    b. Single Line - £ 40 : All numbers in any one row are striked off <br />
    c. Double Line - £ 60 : All numbers any of the two rows are striked off <br />
    d. Full House - £ 70 : If all the numbers are striked off <br />

## Windfalls Being Introduced
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



## Hypothesis or hypotheses before running the simulation:

#### "The pay-out amount for each windfall must be double the price of the ticket." 

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

As of 04/25 : <br />

ticket_genertor.py creates and displays the type of ticket specified. <br />
The ticket generated goes strictly with the design of an actual ticket. Each generated ticket has 3 rows, 9 columns, 15 non duplicate numbers, 5 numbers in each row, 4 spaces in each row.<br />
To see a sample ticket, simply run the program.<br />
<br />
bingo_game.py allows to find the winners for usual 4 winning combinations (not windfalls yet). Presently, a hard coded ticket is used to test the functionality of the class.<br />
To see how the game goes, simply run the file.<br />


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

