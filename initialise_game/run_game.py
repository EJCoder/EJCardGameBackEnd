from initialise_game.create_deck import CreateDeck
from initialise_game.play_card import PlayCard
from initialise_game.deal_cards import DealCards


if __name__ == '__main__':
    create_deck = CreateDeck(1)
    deck = create_deck.create_shuffled_deck()
    deal_cards = DealCards(deck, 3, 5)
    players_and_cards, playing_deck = deal_cards.cards_deal()
    discarded_pile = []
    play_cards = PlayCard(deck, discarded_pile, players_and_cards)
    print(players_and_cards[0])

    print("Joe your cards are " + str(players_and_cards[0]["hand"]))
    print("Sexy Man your cards are " + str(players_and_cards[1]["hand"]))
    print("Silly man your cards are " + str(players_and_cards[2]["hand"]))
    print("Joe play cards if desired")
    joe_discarded_cards_string = input()
    joe_discarded_cards = joe_discarded_cards_string.split(", ")
    play_cards.play_card("Player 1", joe_discarded_cards)
    play_cards.pickup_card("Player 1", len(joe_discarded_cards))
    print("Sexy man play cards if desired")
    eoghan_discarded_cards_string = input()
    eoghan_discarded_cards = eoghan_discarded_cards_string.split(", ")
    play_cards.play_card("Player 2", eoghan_discarded_cards)
    play_cards.pickup_card("Player 2", len(eoghan_discarded_cards))
    print("Silly man play cards if desired")
    eamon_discarded_cards_string = input()
    eamon_discarded_cards = eamon_discarded_cards_string.split(", ")
    play_cards.play_card("Player 3", eamon_discarded_cards)
    play_cards.pickup_card("Player 3", len(eamon_discarded_cards))
    print(players_and_cards)




