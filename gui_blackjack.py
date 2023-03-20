
#Presentation tier of the Blackjack game
#Implement playerCanPlayTurn method and play, hit and stand event handlers

#Assignment: Phase 3 project
#Class: PROG 128
#Date: (March 17 , 2023)
#Author: Nam Nguyen
#Description: Phase 3 part of the project. 


import tkinter as tk
from tkinter import ttk

from blackjack import Blackjack

from objects import Card, Hand, Deck

STARTING_BALANCE = 100
class BlackjackFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        # Define string variables for text entry fields
        self.money = tk.StringVar()
        self.bet = tk.StringVar()
        self.dealerCards = tk.StringVar()
        self.dealerPoints = tk.StringVar()
        self.playerCards = tk.StringVar()
        self.playerPoints = tk.StringVar()
        self.result = tk.StringVar()


        # Initialize game variables
        self.game = Blackjack(STARTING_BALANCE)
        self.gameOver = True

        # Inititalize components
        self.initComponents()

        # Display current money amount
        self.money.set("$"+str(self.game.money))

        #Initialize bet to 0
        self.bet.set("0")

    def initComponents(self):
        self.pack()
        
        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Money:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.money,
                  state="readonly").grid(
            column=1, row=0, sticky=tk.W)

        ttk.Label(self, text="Bet:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.bet).grid(
            column=1, row=1, sticky=tk.W)

        ttk.Label(self, text="DEALER").grid(
            column=0, row=2, sticky=tk.E)
        
        ttk.Label(self, text="Cards:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=50, textvariable=self.dealerCards,
                  state="readonly").grid(
            column=1, row=3, sticky=tk.W)

        ttk.Label(self, text="Points:").grid(
            column=0, row=4, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.dealerPoints,
                  state="readonly").grid(
            column=1, row=4, sticky=tk.W)

        ttk.Label(self, text="YOU").grid(
            column=0, row=5, sticky=tk.E)
        
        ttk.Label(self, text="Cards:").grid(
            column=0, row=6, sticky=tk.E)
        ttk.Entry(self, width=50, textvariable=self.playerCards,
                  state="readonly").grid(
            column=1, row=6, sticky=tk.W)

        ttk.Label(self, text="Points:").grid(
            column=0, row=7, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.playerPoints,
                  state="readonly").grid(
            column=1, row=7, sticky=tk.W)

        self.makeButtons1()

        ttk.Label(self, text="RESULT:").grid(
            column=0, row=9, sticky=tk.E)
        ttk.Entry(self, width=50, textvariable=self.result,
                  state="readonly").grid(
            column=1, row=9, sticky=tk.W)

        self.makeButtons2()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons1(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=1, row=8, sticky=tk.W)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Hit", command=self.hit) \
            .grid(column=0, row=0)
        ttk.Button(buttonFrame, text="Stand", command=self.stand) \
            .grid(column=1, row=0)

    def makeButtons2(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=1, row=10, sticky=tk.W)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Play", command=self.play) \
            .grid(column=0, row=0)
        ttk.Button(buttonFrame, text="Exit", command=self.exit) \
            .grid(column=1, row=0)


    ''' Method to update the dealer hand and the dealer points in the GUI'''
    def displayDealer(self):
        if self.game.dealerHand != None:
            cards = self.game.dealerHand.shortDisplay()
            self.dealerCards.set(cards)
            self.dealerPoints.set(str(self.game.dealerHand.points()))         

    ''' Method to update the player hand and the dealer points in the GUI'''
    def displayPlayer(self):
        if self.game.playerHand != None:
            cards = self.game.playerHand.shortDisplay()
            self.playerCards.set(cards)
            self.playerPoints.set(str(self.game.playerHand.points()))        

    ''' Method to update the result of the game
    Calls determineOutcome to decide what the outcome of the game is.
    Updates the result and the money
    '''
    def displayResult(self):
        result = self.game.determineOutcome()
        self.result.set(result)
        self.money.set("$"+str(self.game.money))

    ''' Method confirms that the game is underway and sets result to blank,
    and returns True indicating that player can play a turn (i.e. can
    select hit or stand)
    otherwise if game in not underway, updates result with correct
    feedback, and returns False
    '''
    def playerCanPlayTurn(self):
        if self.gameOver:
            self.result.set("No game underway.")
            return False
        else:
            return True


    ''' Method to implement user selecting to hit.
    Method confirms that user can play a turn, if not returns
    else calls the takePlayerTurn and reports the player state by calling displayPlayer.
    Next checks if player is busted, if so ends the game and updates the result by
    calling displayResult.
    '''
    def hit(self):
        if not self.playerCanPlayTurn():
            return
        self.game.playerHand.addCard(self.game.deck.dealCard())
        self.displayPlayer()
        if self.game.playerHand.isBusted:
            self.gameOver = True
            self.displayDealer()
            self.displayResult()

    ''' Method to implement user selecting to stand.
    Method confirms that user can play a turn, if not returns
    else ends the game and has the dealer play his turn and
    reports the dealer state by calling displayDealer.
    Finally updates the result by calling displayResult.        
    '''
    def stand(self):
        if not self.playerCanPlayTurn():
            return
        self.gameOver = True
        self.game.takeDealerTurn()
        self.displayDealer()
        self.displayResult()

            
    ''' Method to start a new game.
    Method checks that the game is not already underway, if so does nothing and returns
    Else
        First reads the bet amount and verifies that it is valid (it is greater than
            0 and less than the money available), if not valid, gives feedback by updating
            the result textEntry and returns
        Next starts the game by
            - making sure gameOver is set to False
            - setting the bet on the game
            - calling setupRound
            - displaying the player's cards and points
            - displaying the dealer's card and points
        Before returning checks if either player has a blackjack, if so ends the game 
    '''
    def play(self):
        if not self.gameOver:
            return

        try:
            bet = int(self.bet.get())

            if bet <= 0 or bet > self.game.money:
                self.result.set("Invalid bet amount")
                return

            elif bet > self.game.money:
                self.result.set("Invalid bet amount. You don't have enough money to make this bet")
                return
        except ValueError:
            self.result.set("Invalid bet amound. Bet must be a valid interger.")
            return

        self.gameOver = False
        self.game.bet = bet
        self.game.setupRound()
        self.displayPlayer()
        self.displayDealer()

        if self.game.playerHand.hasBlackjack:
            self.gameOver = True
            self.displayResult()
        elif self.game.dealerHand.hasBlackjack:
            self.gameOver = True
            self.displayResult()



    def exit(self):
        self.parent.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Blackjack")
    BlackjackFrame(root)
    root.mainloop()
