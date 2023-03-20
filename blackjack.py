
#Assignment: Phase 3 project
#Class: PROG 128
#Date: (March 16 , 2023)
#Author: Nam Nguyen
#Description: Phase 3 part of the project. 

from objects import Card, Deck, Hand

class Blackjack:
    def __init__(self, startingBalance):
        self.money = startingBalance
        self.bet = 0
        self.deck = None
        self.dealerHand = None
        self.playerhand = None

    def displayCards(self,hand, title):
        print()
        print(title)
        print()
        print(f"{hand}Points: {hand.points()}\n")
        print()
        
    def getBet(self):
        while True:
                bet = int(input("Bet amount: "))
                if bet <= 0:
                    print("Invalid amount. Enter a positive number")
                elif bet > self.money:
                    print("You don't have enough money to make that bet.")
                else:
                    self.bet = bet
                    break

    def setupRound(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealerHand = Hand()
        self.playerHand = Hand()
        self.playerHand.addCard(self.deck.dealCard())
        self.playerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())
        self.displayCards(self.dealerHand, "Dealer's SHOW CARD:")
        self.displayCards(self.playerHand, "YOUR CARDS: ")
        
    def takePlayerTurn(self):
        while True:
            action = input("Hit or stand? (h for hit or s for stand): ")
            if action.lower() == 's':
                self.displayCards(self.playerHand, "YOUR CARDS:")
                break
            elif action.lower() == 'h':
                card = self.deck.dealCard()
                self.playerHand.addCard(card)
                self.displayCards(self.playerHand, "YOUR CARDS:")
                if self.playerHand.isBusted:
                    print("Busted!")
                    self.displayCards(self.playerHand, "YOUR CARDS:")
                    break
            else:
                print("Invalid input. Please enter h or s.")

    def takeDealerTurn(self):
        self.dealerHand.addCard(self.deck.dealCard())
        while self.dealerHand.points() < 17:
            card = self.deck.dealCard()
            self.dealerHand.addCard(card)
            self.displayCards(self.dealerHand, "DEALER'S CARDS:")
            if self.dealerHand.isBusted:
                print("Dealer Busted!")
                self.displayCards(self.dealerHand, "DEALER'S CARDS:")
                break
            elif self.dealerHand.hasBlackjack:
                print("Dealer has a blackjack!")
                self.displayCards(self.dealerHand, "DEALER'S CARDS:")
                break

    def determineOutcome(self):
        if self.playerHand.isBusted:
            self.money -= self.bet
            return "Sorry. You busted. You lose."
        elif self.dealerHand.isBusted:
            self.money += self.bet
            return "Yay! The dealer busted. You win!"
        elif self.playerHand.hasBlackjack and not self.dealerHand.hasBlackjack:
            self.money += 1.5 * self.bet
            return "Blackjack! You win!"
        elif self.dealerHand.hasBlackjack and not self.playerHand.hasBlackjack:
            self.money -= self.bet
            return "Dealer blackjack. You lose."
        elif self.playerHand.points() > self.dealerHand.points():
            self.money += self.bet
            return "Hooray! You win!"
        elif self.playerHand.points() < self.dealerHand.points():
            self.money -= self.bet
            return "Sorry. You lose."
        else:
            return "You push."

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    # initialize starting money
    money = 100
    print("Starting Balance:", money)

    # instantiate object of Blackjack class 
    blackjack = Blackjack(money)
    
    print("Setting up a round...")
    blackjack.getBet()
    blackjack.setupRound()

    print("Playing Player Hand...")
    blackjack.takePlayerTurn()

    print("YOUR POINTS:",blackjack.playerHand.points())
    print("Good bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
