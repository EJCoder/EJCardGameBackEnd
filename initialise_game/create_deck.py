import random

def card_deck(number=1):
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
            # playing_deck.append(card)

    for i in range(number):
        add_deck = deck.copy()  # originally doubled the size of the deck for every 1+ increase in "number"
        playing_deck.extend(add_deck)  # added a second deck list to insure the above was resolved (no iteration
        # accumulation)
    return playing_deck


def shuffle_cards(number=1):
    playing_deck = card_deck(number)
    random.shuffle(playing_deck)
    return playing_deck


def cards_deal(number_of_players, number_of_cards, playing_cards):
    players_list = []
    players_cards = []
    for player_number in range(number_of_players):
        players_list.append("Player " + str(player_number+1))
        player_card = random.sample(playing_cards, number_of_cards)
        for card in player_card:
            playing_cards.remove(card)
        players_cards.append(player_card)

    return players_list, players_cards



if __name__ == "__main__":
    playing_cards = shuffle_cards()
    players_list, players_cards = cards_deal(1, 1, playing_cards)
