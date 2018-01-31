import collections
import random

'''
namedtuple用于构建只有少数属性但没有方法的对象
'''
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

suit_values=dict(spades=3,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    """
    给每一张牌计算一个优先值
    :param card:
    :return:
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value* len(suit_values)+suit_values[card.suit]


# ===================test()================== #
beercard = Card('7', 'diamonds')
print(beercard)

deck = FrenchDeck()
print(len(deck))

print(random.choice(deck))
print([deck[i] for i in range(0, 52)])
print(deck[12::13])

for card in deck:
    print(card)

print(len(suit_values))

for card in sorted(deck,key=spades_high):
    print(card)