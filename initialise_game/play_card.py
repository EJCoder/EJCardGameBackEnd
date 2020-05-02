class PlayCard:
    def __init__(self, deck, discarded_pile, players_and_cards):
        self.deck = deck
        self.discarded_pile = discarded_pile
        self.players_and_cards = players_and_cards

    def pickup_card(self, player, number_of_cards):
        for player_and_cards in self.players_and_cards:
            if player_and_cards['name'] == player:
                cards_to_pick_up = self.deck[0:number_of_cards]
                player_and_cards['hand'].extend(cards_to_pick_up)
                self.deck = self.deck[number_of_cards:]
                break

    def play_card(self, player, cards):
        for player_and_cards in self.players_and_cards:
            if player_and_cards["name"] == player:
                cards_to_play = cards
                for card in cards_to_play:
                    player_and_cards["hand"].remove(card)
                self.discarded_pile.extend(cards_to_play)
                break







