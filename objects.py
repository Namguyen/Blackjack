



import random


class Card:
    RANKORDER = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    SUITORDER = ["Spades", "Hearts", "Diamonds", "Clubs"]
    SUITSYMBOLS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        if self.rank == "Ace":
            return 11
        elif self.rank in ["Jack", "Queen", "King"]:
            return 10
        else:
            return int(self.rank)
        
    def __lt__(self, other):
        if self.SUITORDER.index(self.suit) > self.SUITORDER.index(other.suit):
            return True
        elif self.SUITORDER.index(self.suit) == self.SUITORDER.index(other.suit):
            return self.RANKORDER[self.rank] < self.RANKORDER[other.rank]
        else:
            return False
        
    def __str__(self):
        return f"{self.rank} {Card.SUITSYMBOLS[self.suit]}"

class Deck:
    def __init__(self):
        self.__deck = [Card(rank, suit) for suit in Card.SUITORDER for rank in Card.RANKORDER.keys()]

    def shuffle(self):
        random.shuffle(self.__deck)

    def dealCard(self):
        return self.__deck.pop()

    def __len__(self):
        return len(self.__deck)

    def __iter__(self):
        return iter(self.__deck)

class Hand:
    def __init__(self):
        self.__cards = []

    def addCard(self, card):
        self.__cards.append(card)

    def points(self):
        total_points = 0
        aces_count = 0
        for card in self.__cards:
            if card.rank == "Ace":
                aces_count += 1
            total_points += card.value
        while aces_count > 0 and total_points > 21:
            total_points -= 10
            aces_count -= 1
        return total_points

    @property
    def isBusted(self):
        return self.points() > 21

    @property
    def hasBlackjack(self):
        return len(self.__cards) == 2 and self.points() == 21

    def shortDisplay(self):
        sorted_cards = sorted(self.__cards)
        return " ".join(str(card) for card in sorted_cards)

    def __str__(self):
        sorted_cards = sorted(self.__cards)
        cards_str = ""
        for card in sorted_cards:
            cards_str += f"{card}\n"
        return cards_str

    def __len__(self):
        return len(self.__cards)

    def __iter__(self):
        return iter(self.__cards)

def main():
    print("Cards - Tester")
    print()

    
    testcardsList = [Card("Ace", "Spades"), Card("Queen", "Hearts"), Card("10", "Clubs"),
             Card("3", "Diamonds"), Card("Jack", "Hearts"), Card("7", "Spades")]
    testcardsList.sort()
    print("TEST CARDS LIST AFTER SORTING.")
    for c in testcardsList:
        print(c)
    print()

    
    print("DECK")
    deck = Deck()
    print("Deck created.")
    deck.shuffle()    
    print("Deck shuffled.")
    print("Deck count:", len(deck))
    print()

    
    hand = Hand()
    for i in range(10):
        hand.addCard(deck.dealCard())

    print("SORTED HAND")
    print()
    print(hand)

    print()
    print("Hand points:", hand.points())
    print("Hand count:", len(hand))
    print("Deck count:", len(deck))

if __name__ == "__main__":
    main()

