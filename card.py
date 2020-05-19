import random
class card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def show(self):
        print("{} of {}".format(self.value, self.suit))
class deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ["Hearts", "Spades", "Clubs", "Diamonds"]:
            for a in range(1,14):
                self.cards.append(card(s,a))
    def show(self):
        for card in self.cards:
            card.show()
    def shuffle(self):
        total_num = len(self.cards)
        print(total_num)
        for j in range(total_num-1,0):
            onecard = randint(0,j)
            if j==onecard:
                continue
            self.cards[j],self.cards[onecard]=self.cards[onecard],self.cards[j]
            print(self.cards[j])
            print(self.cards[onecard])
dec = deck()
dec.shuffle()
