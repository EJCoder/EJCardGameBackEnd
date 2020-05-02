class PlayCard:
    def __init__(self, deck, discarded_pile, players_and_cards):
        self.deck = deck
        self.discarded_pile = discarded_pile
        self.players_and_cards = players_and_cards

    def pickup_card(self, player, number_of_cards):
        for player_and_cards in players_and_cards:
            if player_and_cards['player'] == player:
                cards_to_pick_up = self.deck[0:number_of_cards]
                player_and_cards['cards'].extend(cards_to_pick_up)
                self.deck = self.deck[number_of_cards:]
                continue

    def play_card(self, player):


if __name__ == '__main__':
    deck = ['card_1', 'card_2', 'card_3', 'card_4']
    discarded_pile = []
    players_and_cards = [
        {
            'player': 'player_1',
            'cards': ['player_1_card_1', 'player_1_card_2']
        },
        {
            'player': 'player_2',
            'cards': ['player_2_card_1', 'player_2_card_2']
        }
    ]
    players = ["p1", "p2", "p3"]
    cards = [["c1", "c2", "c7"], ["c3", "c4"], ["c5", "c6"]]
    cards.append(["bhfudjas"])
    players_and_cards = [
        {
            'player': 'p1',
            'cards': ['c1', 'c2', 'c7']
        },
        {
            'player': 'p2',
            'cards': ['c3', 'c4']
        },
        {
            'player': 'p3',
            'cards': ['c5', 'c6']
        }
    ]

    play_card = PlayCard(deck, discarded_pile, players_and_cards)
