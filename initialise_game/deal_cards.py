import random

class DealCards():
    def __init__(self, deck, number_of_players):
        self.deck = deck
        self.number_of_players = number_of_players

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
