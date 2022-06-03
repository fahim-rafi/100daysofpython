import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_hand():
    hand = random.sample(cards, k=2)
    return hand


def computer_hand():
    hand = random.sample(cards, k=2)
    return hand


def display_score(p_hand, c_hand):
    print(
        f"Your cards: {p_hand}, current score: {sum(p_hand)}\nComputer's first card: {c_hand[0]}")


p_hand = start_hand()
c_hand = computer_hand()

display_score(p_hand, c_hand)

take_card = input("Press 'y' to get another card, 'n' to pass: ")


def deal(p_hand):
    pick = random.choice(cards)
    p_hand.append(pick)
    return p_hand


if take_card == 'y':
    print(deal(p_hand))

display_score(p_hand, c_hand)
# def deal():
