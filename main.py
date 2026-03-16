'''
Zane Parmenter's Awesome Cool Slot Machine
Put together in the final few hours of the final day (3/15/2026)
Pray forgive my sins.
'''
#IMPORTS the RANDOM library because this is a SLOT MACHINE and they are RANDOM
import random
#VARIABLES to set ROWS and COLUMNS. I do not use these. But YOU can.
rows = 1
columns = 3
#OPENS a DICTIONARY to set how FREQUENT symbols are
symbol_count = {
    "7️⃣": 1,
    "⭐": 2,
    "♣️": 4,
    "🍒": 8
}
#OPENS a DICTIONARY to set how VALUABLE symbols are
symbol_value = {
    "7️⃣": 16,
    "⭐": 8,
    "♣️": 4,
    "🍒": 2
}
#CHECKS how much you WIN based off symbol value
def checkWinnings(columns, bet, values):
#SETS current WINNINGS back to ZERO for FRESH MONEY
    winnings = 0
    for line in range(rows):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
    return winnings
#DEFINES how much MONEY you choose to START with
def deposit():
#SET AMOUNT to 0 so I can avoid WHILE TRUE
    amount = 0
    while amount not in [1-1000]:
        amount = input("What would you like to deposit? You have $1000.\n")
    #VALIDATE AMOUNT VARIABLE
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                if amount <= 1000:
                    break
                else:
                    print("You are not that rich.")
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number")
    return amount
#THIS is the BIG ONE. It SPINS the SLOTS and gives you the RESULT in COLUMNS
def getSpins(rows, cols, symbols):
    allSymbols = []
    for sym, count in symbols.items():
        for _ in range(count):
            allSymbols.append(sym)
    columns = []
    for _ in range(cols):
        currentSymbols = allSymbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
#PRINTS the SLOT MACHINE COLUMN by COLUMN
def printSlots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        print()
#DEFINES how much you BET on a roll
def getBet():
#BET 0 for REFRESHING PURPOSES
    bet = -1
#MAX and MIN bet for FUN PURPOSES
    maxBet = 100
    minBet = 1
    while bet == -1:
        amount = input("What would you like to bet? (1-100 Chips) (0 to quit)\n")
        if amount.isdigit():
            amount = int(amount)
        #QUIT EASY
            if amount == 0:
                quit()
            elif minBet <= amount <= maxBet:
                break
            else:
                print(f"Amount must be between 1 and 100 chips.")
        else:
            print("Please enter a valid number")
    return amount
#MAIN
def main():
#SETS REPLAY VARIABLE (1 time only)
    play = True
#RUNS DEPOSIT FUNCTION and SETS BALANCE
    balance = deposit()
#SETS SPIN_COUNT VARIABLE
    spinCount = 0
#CENTRAL GAMEPLAY LOOP (NOT a while True)
    while play:
    #INCREASE SPIN COUNT
        spinCount += 1
        print(f"Spin: {spinCount} | Current balance: {balance} chips")
    #RUNS GET BET FUNCTION
        bet = getBet()
        if bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: {balance} chips")
        print(f"You are betting {bet} chips.")
    #SETS SLOTS VARIABLE via GETSPINS FUNCTION
        slots = getSpins(rows, columns, symbol_count)
    #PRINTS the SLOTS
        printSlots(slots)
    #SETS your WINNINGS VARIABLE based on CHECKWINNINGS FUNCTION
        winnings = checkWinnings(slots, bet, symbol_value)
    #SETS your BALANCE by subtracting WINNINGS and BET
        balance += winnings - bet
        print(f"You won {winnings} chips.")
    #INPUT to see if you STILL WANT TO PLAY
        play = input("Would you like to keep playing? (y/n) ").lower()
        if play == "y":
            print("Good luck.")
            play = True
        elif play == "n":
            print("You leave with "+str(balance)+" chips.")
            play = False
#RUNS PROGRAM
main()
