import random


class Deck:
    # Static lists of suits and card values used for all instances of Deck.
    suits = ["H", "D", "C", "S"]  # Hearts, Diamonds, Clubs, Spades
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]  # 2-10, Jack, Queen, King, Ace

    def __init__(self):
        self.cards = []  # Initialize an empty list for the deck's cards
        self.fill_deck()  # Fill the deck with cards upon creation

    def fill_deck(self):
        # Populates the deck with all possible card combinations of suits and values
        for suit in Deck.suits:
            for value in Deck.values:
                card = value + suit  # Combines value and suit into a single string
                self.cards.append(card)  # Adds the card to the deck

    def shuffle(self):
        # Randomly shuffles the cards in the deck
        random.shuffle(self.cards)

    def deal(self, n):
        # Deals 'n' cards from the deck
        dealt_cards = []  # List to store the dealt cards

        for i in range(n):
            if len(self.cards) == 0:
                break  # Stop dealing if the deck is empty

            card = self.cards.pop()  # Remove the last card from the deck
            dealt_cards.append(card)  # Add the removed card to the dealt cards list

        return dealt_cards  # Return the list of dealt cards

    def sort_by_suit(self):
        # Sorts the remaining cards in the deck by suit
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.cards:
            suit = card[-1]  # Extracts the suit which is the last character in the card string
            cards_by_suit[suit].append(card)  # Append card to the corresponding suit list

        # Concatenate lists of cards from each suit to form the sorted deck
        self.cards = (
                cards_by_suit["H"] +
                cards_by_suit["D"] +
                cards_by_suit["C"] +
                cards_by_suit["S"]
        )

    def contains(self, card):
        # Checks if a specific card is in the deck
        return card in self.cards

    def copy(self):
        # Returns a new Deck instance with a copy of the current deck's cards
        new_deck = Deck()
        new_deck.cards = self.cards[:]  # Copy the cards using list slicing
        return new_deck

    def get_cards(self):
        # Returns a copy of the deck's cards list
        return self.cards[:]

    def __len__(self):
        # Returns the number of cards left in the deck
        return len(self.cards)
