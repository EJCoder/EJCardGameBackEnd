import unittest

from EJFirstDirectory.create_deck import card_deck, shuffle_cards, cards_deal

ordered_deck = ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts', 'A of Hearts', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds', 'A of Diamonds', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades', 'A of Spades', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs', 'A of Clubs']
two_ordered_decks = ordered_deck + ordered_deck


class TestCardDeck(unittest.TestCase):

    def test_single_card_deck(self):
        deck = card_deck(1)
        self.assertEqual(
            deck,
            ordered_deck,
            "Should be: ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', "
            "'8 of Hearts', '9 of Hearts', '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts', 'A of Hearts', "
            "'2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', "
            "'8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds', "
            "'A of Diamonds', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', "
            "'7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades', "
            "'A of Spades', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', "
            "'8 of Clubs', '9 of Clubs', '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs', 'A of Clubs']"
        )

    def test_multiple_card_deck(self):
        deck = card_deck(2)
        self.assertEqual(
            deck,
            two_ordered_decks,
            "Should be: ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', "
            "'8 of Hearts', '9 of Hearts', '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts', 'A of Hearts', "
            "'2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', "
            "'8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds', "
            "'A of Diamonds', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', "
            "'7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades', "
            "'A of Spades', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', "
            "'8 of Clubs', '9 of Clubs', '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs', 'A of Clubs', "
            "'2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', "
            "'8 of Hearts', '9 of Hearts', '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts', 'A of Hearts', "
            "'2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', "
            "'8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds', "
            "'A of Diamonds', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', "
            "'7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades', "
            "'A of Spades', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', "
            "'8 of Clubs', '9 of Clubs', '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs', 'A of Clubs']"
        )

    def test_length_single_card_deck(self):
        deck = card_deck(1)
        self.assertEqual(len(deck), 52, "Should be: 52")

    def test_length_multiple_card_deck(self):
        deck = card_deck(4)
        self.assertEqual(len(deck), 208, "Should be: 208")


# TODO check length of shuffled deck
class TestShuffleCards(unittest.TestCase):

    def sample_test_1(self):
        self.assertEqual(1, 1, "Should be: sample")


four_playing_cards = ['card_1', 'card_2', 'card_3', 'card_4']


class TestCardDeal(unittest.TestCase):

    def test_card_deal_single_player_single_card(self):
        players_list, players_cards = cards_deal(1, 1, four_playing_cards)
        self.assertEqual(len(players_list), 1, "Should be: sample")
        self.assertEqual(len(players_cards), 1, "Should be: sample")
        self.assertEqual(len(players_cards[0]), 1, "Should be: sample")

    def test_card_deal_multiple_player_single_card(self):
        players_list, players_cards = cards_deal(2, 1, four_playing_cards)
        self.assertEqual(len(players_list), 2, "Should be: 2")
        self.assertEqual(len(players_cards), 2, "Should be: 2")
        self.assertEqual(len(players_cards[0]), 1, "Should be: 1")
        self.assertEqual(len(players_cards[1]), 1, "Should be: 1")

    # TODO test multiple players multiple cards (change name of function)
    def sample_test_1(self):
        self.assertEqual(1, 1, "Should be: sample")

    # TODO test single player multiple cards (change name of function)
    def sample_test_2(self):
        self.assertEqual(1, 1, "Should be: sample")

    # TODO for two players they never get the same card  (change name of function)
    def sample_test_3(self):
        self.assertEqual(1, 1, "Should be: sample")


if __name__ == '__main__':
    unittest.main()
