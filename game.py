from asyncio.windows_events import NULL
from numpy.core.fromnumeric import size
import pygame, sys
import numpy as np
import random as rand
import time

from pygame import font
from player import *
from tkinter import *
import tkinter as tk

pygame.init()

WIDTH = 900
HEIGHT = 600
LINE_WIDTH = 5
BACKGROUND_COLOR = (255,255,255)
LINE_COLOR = (53,57,53)
BOARD_ROW = 8
BOARD_COLUMN = 12
player = 1

player1CurrPosition = [0,0]
player2CurrPosition = [0,0]
player3CurrPosition = [0,0]
player4CurrPosition = [0,0]

income1 = 0
income2 = 0
income3 = 0
income4 = 0

def create_players(screen, p1, p2, p3, p4):
    global income1
    global income2
    global income3
    global income4
    income1 = p1
    income2 = p2
    income3 = p3
    income4 = p4
    screen.destroy()

def intro_screen():
    introScreen = Tk()
    #cardLabel = Label(cardScreen, text )
    introScreen.title('Player incomes')
    introScreen.geometry("600x600")

    iText = "Please input your player's income"
    introText = Label(introScreen, text=iText)
    introText.config(font =("Courier", 18))
    introText.pack()

    whiteSpace = Label(introScreen, text="")
    whiteSpace.config(font=("Courier", 10))
    whiteSpace.pack()

    p1Text = "Player 1 (RED)"
    introP1Text = Label(introScreen, text=p1Text)
    introP1Text.config(font =("Courier", 18))
    introP1Text.pack()

    input1 = tk.Text(introScreen, height = 1, width = 10, font=("Courier", 18))
    input1.pack()
    
    whiteSpace = Label(introScreen, text="")
    whiteSpace.config(font=("Courier", 10))
    whiteSpace.pack()

    p2Text = "Player 2 (BLUE)"
    introP2Text = Label(introScreen, text=p2Text)
    introP2Text.config(font =("Courier", 18))
    introP2Text.pack()

    input2 = tk.Text(introScreen, height = 1, width = 10, font=("Courier", 18))
    input2.pack()
    
    whiteSpace = Label(introScreen, text="")
    whiteSpace.config(font=("Courier", 10))
    whiteSpace.pack()

    p3Text = "Player 3 (GREEN)"
    introP3Text = Label(introScreen, text=p3Text)
    introP3Text.config(font =("Courier", 18))
    introP3Text.pack()

    input3 = tk.Text(introScreen, height = 1, width = 10, font=("Courier", 18))
    input3.pack()
    
    whiteSpace = Label(introScreen, text="")
    whiteSpace.config(font=("Courier", 10))
    whiteSpace.pack()

    p4Text = "Player 4 (PINK)"
    introP4Text = Label(introScreen, text=p4Text)
    introP4Text.config(font =("Courier", 18))
    introP4Text.pack()

    input4 = tk.Text(introScreen, height = 1, width = 10, font=("Courier", 18))
    input4.pack()
    
    whiteSpace = Label(introScreen, text="")
    whiteSpace.config(font=("Courier", 10))
    whiteSpace.pack()

    finishButton = tk.Button(introScreen, text ="Finish", 
        command = lambda: create_players(introScreen, float(input1.get(1.0, "end-1c")), float(input2.get(1.0, "end-1c")), 
        float(input3.get(1.0, "end-1c")), float(input4.get(1.0, "end-1c"))), width=10,height=3, font =("Courier", 14))
    finishButton.pack()

    introScreen.mainloop()
    
intro_screen()

play1Account = Player(1,income1)
play2Account = Player(2,income2)
play3Account = Player(3,income3)
play4Account = Player(4,income4)

def cardSeparator(whichList):
    tempCard = ""
    cardSep = []
    for cards in whichList:
        
        if ";" not in cards:
            tempCard = tempCard + cards

        else:
            tempList = cards.split(';')
                # initialize an empty string
            tempLine = "" 
            
            # traverse in the string  
            for word in tempList: 
                tempLine += word

            tempCard = tempCard + tempLine
            cardSep.append(tempCard)
            tempCard = ""

    return cardSep
    
topCardsList = open("topcards.txt")
rightCardsList = open("rightcards.txt")
bottomCardsList = open("bottomcards.txt")
leftCardsList = open("leftcards.txt")

boardDict = {}
topRow = cardSeparator(topCardsList)
rightCol = cardSeparator(rightCardsList)
bottomRow = cardSeparator(bottomCardsList)
leftCol = cardSeparator(leftCardsList)

emergencyCards = {}
for i in range(0,6):
    emergencyCards[i] = ""

emergencyCards[0] = "Your wallet is stolen!\n$100 cash LOST!\n"
emergencyCards[1] = "EARTHQUAKE!!\n$780.00 DAMAGE\n"
emergencyCards[2] = "You fall and break your leg!\n$620.00\nWhere did you go?\n"
emergencyCards[3] = "You fall sick!\n$150.00\nWhere did you go?\n"
emergencyCards[4] = "Car accident!\nHospital charge: $1500.00\nFix your car: $300.00\n"
emergencyCards[5] = "FIRE!!\nHouse repair: $650.00"

urgentCards = {}
for i in range(0,8):
    urgentCards[i] = ""

urgentCards[0] = "Your washing machine broke!\nSPEND: $330.00"
urgentCards[1] = "You have to travel to interview for a new job\nSPEND: $70.00"
urgentCards[2] = "BIRTHDAY!!\nIt's a PARTY!\nSPEND: $250.00"
urgentCards[3] = "It's your FRIEND's birthday!\nSPEND: $30.00"
urgentCards[4] = "You have a headache...\nSPEND: $10.00"
urgentCards[5] = "It's CHRISTMAS!\nSPEND: $835.00"
urgentCards[6] = "It's Diwali!\nSPEND: $945.00"
urgentCards[7] = "You need to buy nice clothes for your new job\nSPEND: $340.00"

#print(len(cardSep))
boardDict[0] = {}
#print(len(topRow))
boardDict[0][0] = "Start\n"
for j in range(1,12):
    boardDict[0][j] = topRow[j-1]

for i in range(1,8):
    boardDict[i] = {}
    boardDict[i][11] = rightCol[i-1]

for j in range(1,12):
    boardDict[7][12-j] = bottomRow[12-j-1]

for i in range(1,8):
    boardDict[8-i][0] = leftCol[8-i-1]

#print(boardDict[0][0])
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('BANK GAME')
screen.fill(BACKGROUND_COLOR)

bank_icon = pygame.image.load('graphics/bank.png')
gov_icon = pygame.image.load('graphics/government.png')
dice1 = pygame.image.load('graphics/dice1.png')
dice2 = pygame.image.load('graphics/dice2.png')
dice3 = pygame.image.load('graphics/dice3.png')
dice4 = pygame.image.load('graphics/dice4.png')
dice5 = pygame.image.load('graphics/dice5.png')
dice6 = pygame.image.load('graphics/dice6.png')

whiteBlank = pygame.image.load('graphics/whiteBack.png')
player1 = pygame.image.load('graphics/player1.png')
player2 = pygame.image.load('graphics/player2.png')
player3 = pygame.image.load('graphics/player3.png')
player4 = pygame.image.load('graphics/player4.png')

board = [[[] for i in range(BOARD_COLUMN)] for j in range(BOARD_ROW)]

def getPlayNum(playNum):
    if(playNum == 1):
        return play1Account

    elif(playNum == 2):
        return play2Account

    elif(playNum == 3):
        return play3Account

    else:
        return play4Account

def make_board():

    for row in range(len(board)):

        for column in range(len(board[row])):
            if row == 0 or row == 7 or column == 0 or column == 11:
                board[row][column].append(0)
                board[row][column].append(0)
                board[row][column].append(0)
                board[row][column].append(0)

            else:

                board[row][column].append(-1)
    
def mark_board(row, col, currPosition, player, moved):

    currRow = currPosition[0]
    currCol = currPosition[1]

    if 0 in board[row][col]:
        i = board[row][col].index(0)
        board[row][col][i] = player
    

    if player == 1 and moved == True:
        screen.blit(whiteBlank, (currCol*75+3, currRow*75+3))
        screen.blit(player1, (col*75+3, row*75+3))
        j = board[currRow][currCol].index(player)
        board[currRow][currCol][j] = 0

        currPosition[0] = row
        currPosition[1] = col

    if player == 2 and moved == True:
        screen.blit(whiteBlank, (currCol*75+43, currRow*75+3))
        screen.blit(player2, (col*75+43, row*75+3))
        j = board[currRow][currCol].index(player)
        board[currRow][currCol][j] = 0

        currPosition[0] = row
        currPosition[1] = col

    if player == 3 and moved == True:
        screen.blit(whiteBlank, (currCol*75+3, currRow*75+41))
        screen.blit(player3, (col*75+3, row*75+41))
        j = board[currRow][currCol].index(player)
        board[currRow][currCol][j] = 0

        currPosition[0] = row
        currPosition[1] = col

    if player == 4 and moved == True:
        screen.blit(whiteBlank, (currCol*75+43, currRow*75+41))
        screen.blit(player4, (col*75+43, row*75+41))
        j = board[currRow][currCol].index(player)
        board[currRow][currCol][j] = 0

        currPosition[0] = row
        currPosition[1] = col

    pygame.display.update()

def dice_roll():
    dice = rand.randint(1,6)
    return dice

def dice_animation():
    
    timeEnd = time.time() + 5

    while(time.time() < timeEnd):
        diceAnim = rand.randint(1,6)

        if(diceAnim == 1):
            screen.blit(dice1, (730,435))
            pygame.display.update()
            pygame.time.delay(300)
        
        if(diceAnim == 2):
            screen.blit(dice2, (730,435))
            pygame.display.update()
            pygame.time.delay(300)

        if(diceAnim == 3):
            screen.blit(dice3, (730,435))
            pygame.display.update()
            pygame.time.delay(300)

        if(diceAnim == 4):
            screen.blit(dice4, (730,435))
            pygame.display.update()
            pygame.time.delay(300)

        if(diceAnim == 5):
            screen.blit(dice5, (730,435))
            pygame.display.update()
            pygame.time.delay(300)

        if(diceAnim == 6):
            screen.blit(dice6, (730,435))
            pygame.display.update()
            pygame.time.delay(300)

def payAccount(aBal, playNum, amount):
    play = getPlayNum(playNum)
    play.subtractBalance(amount)
    newText = "Account Balance: $" + str(play.getBalance())
    aBal.config(text=newText)
    aBal.pack()
    

def earnAccount(aBal, playNum, amount):
    play = getPlayNum(playNum)
    play.addBalance(amount)
    newText = "Account Balance: $" + str(play.getBalance())
    aBal.config(text=newText)
    aBal.pack()
        
def show_card(row, col):
    #print("Show card")
    cardScreen = Tk()
    #cardLabel = Label(cardScreen, text )
    cardScreen.title('What is the card?')
    cardScreen.geometry("600x600")
    ctext = boardDict[row][col]
    cardText = Label(cardScreen, text=ctext)
    cardText.config(font =("Courier", 18))
    cardText.pack()

    if("EMERGENCY" in ctext):
        randNum = rand.randint(0,5)
        eText = emergencyCards[randNum]
        emerText = Label(cardScreen, text=eText)
        emerText.config(font =("Courier", 18))
        emerText.pack()

    if("URGENT" in ctext):
        randNum = rand.randint(0,7)
        uText = urgentCards[randNum]
        urText = Label(cardScreen, text=uText)
        urText.config(font =("Courier", 18))
        urText.pack()

    input = tk.Text(cardScreen, height = 1, width = 10, font=("Courier", 18))
    input.pack()
    #print(player)

    whiteSpace = Label(cardScreen, text="")
    whiteSpace.config(font=("Courier", 10))
    whiteSpace.pack()
    pNum = player
    payButton = tk.Button(cardScreen, text ="Pay", command = lambda: payAccount(accBalance, pNum, float(input.get(1.0, "end-1c"))), width=10,height=3, font =("Courier", 14))
    payButton.pack()

    whiteSpace = Label(cardScreen, text="")
    whiteSpace.config(font=("Courier", 10))
    whiteSpace.pack()

    earnButton = tk.Button(cardScreen, text ="Earn", command = lambda: earnAccount(accBalance, pNum, float(input.get(1.0, "end-1c"))), width=10,height=3, font =("Courier", 14))
    earnButton.pack()

    whiteSpace = Label(cardScreen, text="")
    whiteSpace.config(font=("Courier", 18))
    whiteSpace.pack()

    play = getPlayNum(pNum)
    #print(play.getBalance())
    accText = "Account Balance: $" + str(play.getBalance())
    accBalance = Label(cardScreen, text=accText)
    accBalance.config(text=accText,font =("Courier", 18))
    accBalance.pack()
    
    cardScreen.mainloop()

def finishedYear(playerPos):

    set1 = [6,0]
    set2 = [5,0]
    set3 = [4,0]
    set4 = [3,0]
    set5 = [2,0]
    set6 = [1,0]
    
    if (playerPos[1] == 0):

        if(playerPos[0] == 6 or playerPos[0] == 5 or playerPos[0] == 4 or playerPos[0] == 3 or 
        playerPos[0] == 2 or playerPos[0] == 1):
            return True

        else:
            return False

    else:
        return False



def draw_lines():
    #Border lines
    pygame.draw.line(screen, LINE_COLOR, (0,75), (900,75), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (0,525), (900,525), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (75,0), (75,600), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (825,0), (825,600), LINE_WIDTH)
    
    pygame.draw.line(screen, LINE_COLOR, (0,150), (75,150), LINE_WIDTH)

    #Vertical squares
    for i in range(1,7):
        line_vertical = 75*i
        pygame.draw.line(screen, LINE_COLOR, (0,line_vertical), (75,line_vertical), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (825,line_vertical), (900,line_vertical), LINE_WIDTH)

    for i in range(1,11):
        line_horiz = 75*i
        pygame.draw.line(screen, LINE_COLOR, (line_horiz,0), (line_horiz,75), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (line_horiz,525), (line_horiz,600), LINE_WIDTH)
    



draw_lines()
make_board()
#print("All pieces:", board[0][0])
#mainloop
start = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.blit(bank_icon, (100,125))
        screen.blit(gov_icon, (450, 125))

        if(start == 0):
            screen.blit(dice1, (730,435))
            screen.blit(player1, (3,3))
            screen.blit(player2, (43,3))
            screen.blit(player3, (3, 41))
            screen.blit(player4, (43,41))

            mark_board(0,0,player1CurrPosition,1,False)
            mark_board(0,0,player2CurrPosition,2,False)
            mark_board(0,0,player3CurrPosition,3,False)
            mark_board(0,0,player4CurrPosition,4,False)

            play1Account.addIncome()
            play2Account.addIncome()
            play3Account.addIncome()
            play4Account.addIncome()

            start = 1

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos
            diceRoll = 0
            currDice = 0
            diceRolled = False

            if dice1.get_rect(topleft = (730,435)).collidepoint(x, y):
                currDice = 1
                start = 1
                #print("DIce ROLL1")
                diceRoll = dice_roll()
                diceRolled == True

            if dice2.get_rect(topleft = (730,435)).collidepoint(x, y):
                currDice = 2
                start = 1
                #print("DIce ROLL2")
                diceRoll = dice_roll()
                diceRolled == True

            if dice3.get_rect(topleft = (730,435)).collidepoint(x, y):
                currDice = 3
                start = 1
                #print("DIce ROLL3")
                diceRoll = dice_roll()
                diceRolled == True

            if dice4.get_rect(topleft = (730,435)).collidepoint(x, y):
                currDice = 4
                start = 1
                #print("DIce ROLL4")
                diceRoll = dice_roll()
                diceRolled == True

            if dice5.get_rect(topleft = (730,435)).collidepoint(x, y):
                currDice = 5
                start = 1
                #print("DIce ROLL5")
                diceRoll = dice_roll()
                diceRolled == True

            if dice6.get_rect(topleft = (730,435)).collidepoint(x, y):
                currDice = 6
                start = 1
                #print("DIce ROLL6")
                diceRoll = dice_roll()
                diceRolled == True

            #print("Dice:", diceRoll)
            if(diceRoll == 1):
                dice_animation()
                screen.blit(dice1, (730,435))
            if(diceRoll == 2):
                dice_animation()
                screen.blit(dice2, (730,435))
            if(diceRoll == 3):
                dice_animation()
                screen.blit(dice3, (730,435))
            if(diceRoll == 4):
                dice_animation()
                screen.blit(dice4, (730,435))
            if(diceRoll == 5):
                dice_animation()
                screen.blit(dice5, (730,435))
            if(diceRoll == 6):
                dice_animation()
                screen.blit(dice6, (730,435))

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clickedrow = int(mouseY // 75)
            clickedcol = int(mouseX // 75)

            #print("Row:", clickedrow, " Column", clickedcol)

            if(clickedrow == 0 or clickedrow == 7 or clickedcol == 0 or clickedcol == 11):

                #print("Player:", player)
                if(player == 1):
                    if(clickedcol >= 0 and finishedYear(player1CurrPosition)==True):
                        play1Account.addIncome()

                    mark_board(clickedrow, clickedcol, player1CurrPosition, player, True)
                    time.sleep(0.5)
                    show_card(clickedrow, clickedcol)
                    player = 2

                elif(player == 2):

                    if(clickedcol >= 0 and finishedYear(player2CurrPosition)==True):
                        play2Account.addIncome()

                    mark_board(clickedrow, clickedcol, player2CurrPosition, player, True)
                    time.sleep(0.5)
                    show_card(clickedrow, clickedcol)
                    player = 3

                elif(player == 3):

                    if(clickedcol >= 0 and finishedYear(player3CurrPosition)==True):
                        play3Account.addIncome()

                    mark_board(clickedrow, clickedcol, player3CurrPosition, player, True)
                    time.sleep(0.5)
                    show_card(clickedrow, clickedcol)
                    player = 4

                else:

                    if(clickedcol >= 0 and finishedYear(player4CurrPosition)==True):
                        play4Account.addIncome()

                    mark_board(clickedrow, clickedcol, player4CurrPosition, player, True)
                    time.sleep(0.5)
                    show_card(clickedrow, clickedcol)
                    player = 1

    start = start + 1
    pygame.display.update()
