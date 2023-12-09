from collections import defaultdict
import sys

from enum import Enum


CARDS = list(
    reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])
)


class HandType(int, Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


def determine_rank(hand_type: HandType) -> int:
    match hand_type:
        case HandType.HIGH_CARD:
            return 1
        case HandType.ONE_PAIR:
            return 2
        case HandType.TWO_PAIR:
            return 3
        case HandType.THREE_OF_A_KIND:
            return 4
        case HandType.FULL_HOUSE:
            return 5
        case HandType.FOUR_OF_A_KIND:
            return 6
        case HandType.FIVE_OF_A_KIND:
            return 7


def determine_hand_type(hand: str) -> HandType:
    cards = defaultdict(int)
    for card in hand:
        cards[card] += 1

    try:
        _ = cards.pop("J")
    except KeyError:
        pass

    cards = tuple(sorted(cards.values()))

    match len(cards):
        case 0:
            return HandType.FIVE_OF_A_KIND
        case 1:
            return HandType.FIVE_OF_A_KIND
        case 2:
            if cards[0] == 1:
                return HandType.FOUR_OF_A_KIND
            return HandType.FULL_HOUSE
        case 3:
            if cards[0:2] == (1, 1):
                return HandType.THREE_OF_A_KIND
            return HandType.TWO_PAIR
        case 4:
            return HandType.ONE_PAIR
        case _:
            return HandType.HIGH_CARD


class Hand:
    prev: "Hand | None"
    next: "Hand | None"
    type_: HandType
    cards: str
    bid: int

    def __str__(self) -> str:
        return self.cards

    def __repr__(self) -> str:
        return self.__str__()

    def __init__(self, cards: str, bid: int) -> None:
        self.cards = cards
        self.bid = bid
        self.prev = None
        self.next = None
        self.type_ = determine_hand_type(self.cards)


class LinkedList:
    head: Hand | None
    tail: Hand | None

    def __init__(self) -> None:
        self.head = self.tail = None

    def _prepend(self, hand: Hand) -> None:
        if self.head is None:
            self.head = self.tail = hand
            return

        hand.next = self.head
        self.head.prev = hand
        self.head = hand

    def _append(self, hand: Hand) -> None:
        if self.tail is None:
            self.head = self.tail = hand
            return

        hand.prev = self.tail
        self.tail.next = hand
        self.tail = hand

    def add(self, hand: Hand) -> None:
        if self.head == None:
            self.head = self.tail = hand
            return

        curr = self.head
        while curr is not None:
            for i in range(5):
                if CARDS.index(hand.cards[i]) == CARDS.index(curr.cards[i]):
                    continue

                if CARDS.index(hand.cards[i]) > CARDS.index(curr.cards[i]):
                    curr = curr.next
                    break

                if CARDS.index(hand.cards[i]) < CARDS.index(curr.cards[i]):
                    # insert before

                    if curr.prev is None:
                        return self._prepend(hand)

                    curr.prev.next = hand
                    hand.prev = curr.prev
                    hand.next = curr
                    curr.prev = hand
                    return
            else:
                curr = curr.next
        else:
            return self._append(hand)

    def print(self) -> None:
        curr = self.head
        while curr is not None:
            print("\t", curr.cards, f"next={curr.next}", f"prev={curr.prev}")
            curr = curr.next


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        raw_input = [line.strip().split() for line in f.read().strip().splitlines()]

    winnings: dict[HandType, LinkedList] = defaultdict(LinkedList)

    for cards, bid in raw_input:
        hand = Hand(cards, int(bid))
        winnings[hand.type_].add(hand)

    result = 0
    i = 0

    for hand_type in list(sorted(HandType, key=lambda ht: ht.value)):
        print(hand_type)
        winnings[hand_type].print()

        curr = winnings[hand_type].head
        while curr is not None:
            i += 1
            result += curr.bid * i
            curr = curr.next

        print()

    print(result)
