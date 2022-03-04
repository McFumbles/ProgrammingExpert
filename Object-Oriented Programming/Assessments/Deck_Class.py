import random


class Deck:
    suits = ["D", "H", "C", "S"]
    val = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        for suit in Deck.suits:
            for v in Deck.val:
                cards =  v + suit
                self.cards.append(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt_cards = []
        for i in range(n):
          if len(self.cards) == 0:
              break

          cards = self.cards.pop()
          dealt_cards.append(cards)

        return dealt_cards
    
    def sort_by_suit(self):
      cards_dict = {"H": [], "D": [], "C": [], "S": []}

      for cards in self.cards:
        suit = cards[-1]
        cards_dict[suit].append(cards)
      
      self.cards = (
            cards_dict["H"] +
            cards_dict["D"] +
            cards_dict["C"] +
            cards_dict["S"]
        )

    def contains(self, card):
      return card in self.cards
    
    def copy(self):
      n = Deck()
      n.cards = self.cards[:]
      return n
    
    def get_cards(self):
      return self.cards[:]
    
    def __len__(self):
      return len(self.cards)

d = Deck()
d.shuffle()
d.deal(3)
d.contains("4D")


