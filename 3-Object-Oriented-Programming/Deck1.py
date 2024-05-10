import random
import copy


class Deck:
    suits = ["H", "D", "C", "S"]
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card = value + suit
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt = []

        for i in range(n):
            if len(self.cards) == 0:
                break

            card = self.cards.pop()
            dealt.append(card)

        return dealt

    def sort_by_suit(self):
        temp_list = []
        for card in self.cards:
            if "H" in card:
                temp_list.append(card)

        for card in self.cards:
            if "D" in card:
                temp_list.append(card)

        for card in self.cards:
            if "C" in card:
                temp_list.append(card)

        for card in self.cards:
            if "S" in card:
                temp_list.append(card)

        self.cards = temp_list

    def contains(self, card):
        if card in self.cards:
            return True
        else:
            return False

    def copy(self):
        return copy.deepcopy(self)

    def get_cards(self):
        new_list = self.cards[:]
        return new_list

    def __len__(self):
        return len(self.cards)