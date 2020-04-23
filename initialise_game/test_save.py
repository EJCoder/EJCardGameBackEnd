import random
import operator


def card_deck(extra_deck=False, number=0):
    deck = []
    playing_deck = []
    card_faces = []
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    royals = ["J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    for i in range(len(numbers)):
        card_faces.append(numbers[i])

    for j in range(len(royals)):
        card_faces.append(royals[j])

    for k in range(len(suits)):
        for l in range(len(card_faces)):
            card = card_faces[l] + " of " + suits[k]
            deck.append(card)
            playing_deck.append(card)

    if extra_deck:
        for i in range(number):
            add_deck = deck.copy()  # originally doubled the size of the deck for every 1+ increase in "number"
            playing_deck.extend(add_deck)  # added a second deck list to insure the above was resolved (no iteration
            # accumulation)
        return playing_deck
    elif number == 0:
        return playing_deck


def shuffle_cards(extra_deck=False, number=0):
    playing_deck = card_deck(extra_deck, number)
    random.shuffle(playing_deck)
    return playing_deck


def cards_deal(number, number_of_players, number_of_cards):
    if number_of_players == 1:
        shuffled_deck = random.shuffle(how_many_decks(number))
        hand_player_1 = random.sample(shuffled_deck, k=number_of_cards)
        return print(hand_player_1)
    if number_of_players == 2:
        shuffled_deck = random.shuffle(how_many_decks(number))
        hand_player_1 = random.sample(shuffled_deck, k=number_of_cards)
        hand_player_2 = random.sample(shuffled_deck, k=number_of_cards)
        return print(hand_player_1, hand_player_2)


if __name__ == "__main__":
    print(len(card_deck(True, 3)))
