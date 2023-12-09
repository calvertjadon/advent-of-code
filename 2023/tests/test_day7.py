import pytest

from aoc2023.day7 import HandType, LinkedList, determine_hand_type, Hand

@pytest.mark.parametrize("hand,expected", [
    ("22222", HandType.FIVE_OF_A_KIND),
    ("22223", HandType.FOUR_OF_A_KIND),
    ("22233", HandType.FULL_HOUSE),
    ("22234", HandType.THREE_OF_A_KIND),
    ("22334", HandType.TWO_PAIR),
    ("22345", HandType.ONE_PAIR),
    ("23456", HandType.HIGH_CARD),
    ("JJJJJ", HandType.FIVE_OF_A_KIND),
    ("AAAAJ", HandType.FIVE_OF_A_KIND),
    ("AJAJA", HandType.FIVE_OF_A_KIND),
])
def test_determine_hand_type(hand: str, expected: HandType):
    assert determine_hand_type(hand) == expected

def test_add_same_type():
    hand1 = Hand("KKKKK", 1)
    hand2 = Hand("AAAAA", 1)
    hand3 = Hand("22222", 1)
    hand4 = Hand("55555", 1)

    ll = LinkedList()

    print("before")
    ll.print()
    ll.add(hand1)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand2)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand3)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand4)
    print("after")
    ll.print()
    print()

    hands = []

    curr = ll.head
    while curr is not None:
        hands.append(curr)
        curr = curr.next

    assert hands == [hand3, hand4, hand1, hand2]

def test_add_same_type2():
    hand1 = Hand("AAA22", 1)
    hand2 = Hand("22AAA", 1)
    hand3 = Hand("2AAA2", 1)
    hand4 = Hand("A2A2A", 1)

    ll = LinkedList()

    print("before")
    ll.print()
    ll.add(hand1)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand2)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand3)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand4)
    print("after")
    ll.print()
    print()

    hands = []

    curr = ll.head
    while curr is not None:
        hands.append(curr)
        curr = curr.next

    assert hands == [hand2, hand3, hand4, hand1]

def test_jokers():
    hand1 = Hand("AJAJA", 1)
    hand2 = Hand("JAJAJ", 1)
    hand3 = Hand("AAAAJ", 1)
    hand4 = Hand("JJJJA", 1)
    hand5 = Hand("AAAAA", 1)
    hand6 = Hand("JJJJJ", 1)

    ll = LinkedList()

    print("before")
    ll.print()
    ll.add(hand1)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand2)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand3)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand4)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand5)
    print("after")
    ll.print()
    print()

    print("before")
    ll.print()
    ll.add(hand6)
    print("after")
    ll.print()
    print()

    hands = []

    curr = ll.head
    while curr is not None:
        hands.append(curr)
        curr = curr.next

    assert hands == [hand6, hand4, hand2, hand1, hand3, hand5]

