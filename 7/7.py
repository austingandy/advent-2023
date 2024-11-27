from collections import defaultdict
from enum import IntEnum

cards = 'A K Q T 9 8 7 6 5 4 3 2 J'[::-1].split(' ')
ranks = {c: i for i, c in enumerate(cards)}


class Card:
    def __init__(self, val):
        self.val = val
        self.rank = ranks[val]

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __hash__(self):
        return hash(self.val)

    def __str__(self):
        return f"{self.val}"


class Rank(IntEnum):
    HIGH = 1
    PAIR = 2
    TWO_PAIR = 3
    TRIPLE = 4
    FULL_HOUSE = 5
    QUAD = 6
    FIVE = 7


class Hand:
    def __init__(self, cards, bid):
        self.bid = bid
        self.ranks = {}
        self.cards = cards
        self.ranks = defaultdict(int)
        for c in cards:
            self.ranks[c.val] += 1
        self.counts = defaultdict(list)
        max_count, freq_card = 0, ''
        for k, v in self.ranks.items():
            if v > max_count and k != 'J':
                freq_card = k
                max_count = v
        self.ranks[freq_card] += self.ranks['J']
        del self.ranks['J']
        for k, v in self.ranks.items():
            self.counts[v].append(k)
        if self.counts[5]:
            self.rank = Rank.FIVE
        elif self.counts[4]:
            self.rank = Rank.QUAD
        elif self.counts[3]:
            if self.counts[2]:
                self.rank = Rank.FULL_HOUSE
            else:
                self.rank = Rank.TRIPLE
        elif self.counts[2]:
            if len(self.counts[2]) == 2:
                self.rank = Rank.TWO_PAIR
            else:
                self.rank = Rank.PAIR
        else:
            self.rank = Rank.HIGH

    def __str__(self):
        return ''.join([str(c) for c in self.cards]) + f" {self.bid=}"

    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        for i in range(len(self.cards)):
            if self.cards[i] == other.cards[i]:
                continue
            return self.cards[i] < other.cards[i]
        return False

    def __gt__(self, other):
        if self.rank != other.rank:
            return self.rank > other.rank
        for i in range(len(self.cards)):
            if self.cards[i] == other.cards[i]:
                continue
            return self.cards[i] > other.cards[i]
        return False

    def __eq__(self, other):
        return not self < other and not self > other


def new_hand(s, bid):
    return Hand([Card(c) for c in s], bid)

with open("input.txt", "r") as file:
    s = file.readlines()

hands = []
for l in s:
    line = l.split(' ')
    cards = line[0]
    bid = int(line[1])
    hands.append(Hand([Card(c) for c in cards], bid))

print(new_hand('J2JJJ', 0).rank)

sorted_hands = sorted(hands)
total = 0
for i in range(len(sorted_hands)):
    total += sorted_hands[i].bid*(i+1)

print(total)
