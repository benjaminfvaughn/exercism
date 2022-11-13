"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    rounds = []

    for x in range(3):
        rounds.append(number + x)

    return rounds

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    sum_of_hand = 0

    for x in hand:
        sum_of_hand = sum_of_hand + x

    return sum_of_hand / len(hand)

def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    first_last_avg = (hand[len(hand)-1] + hand[0])/2

    middle_avg = hand[int((len(hand)-1)/2)]

    return (first_last_avg == card_average(hand)) or (middle_avg == card_average(hand))

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand. return: bool - are even and odd averages equal?
    """

    even_sum = 0
    even_cnt = 0

    for x in range(0, len(hand), 2):
        even_sum = even_sum + hand[x]
        even_cnt +=1

    even_avg = even_sum / even_cnt

    odd_sum = 0
    odd_cnt = 0

    for x in range(1, len(hand), 2):
        odd_sum = odd_sum + hand[x]
        odd_cnt +=1

    odd_avg = odd_sum / odd_cnt

    return even_avg == odd_avg

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1]*2

    return hand
