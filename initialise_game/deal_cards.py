import random
from initialise_game.create_deck import CreateDeck

class DealCards():
    def __init__(self, deck, number_of_players, number_of_cards):
        self.deck = deck
        self.number_of_players = number_of_players
        self.number_of_cards = number_of_cards

    def cards_deal(self):
        players_and_cards = []
        for player_number in range(self.number_of_players):
            player_and_cards = {}
            player_name = "Player " + str(player_number+1)
            player_card = self.deck[0:self.number_of_cards]
            player_and_cards["name"] = player_name
            player_and_cards["hand"] = player_card
            for card in player_card:
                self.deck.remove(card)
            players_and_cards.append(player_and_cards)

        return players_and_cards, self.deck

if __name__ == '__main__':
    create_deck = CreateDeck(2)
    playing_deck = create_deck.create_shuffled_deck()

    deal_cards = DealCards(playing_deck, 2, 5)
    dealt_cards = deal_cards.cards_deal()
    players_and_cards, deck = dealt_cards
    print(players_and_cards)

