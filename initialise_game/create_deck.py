import random


class CreateDeck:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks

    def create_deck(self):
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

        for i in range(self.number_of_decks):
            add_deck = deck.copy()  # originally doubled the size of the deck for every 1+ increase in "number"
            playing_deck.extend(add_deck)  # added a second deck list to insure the above was resolved (no iteration
            # accumulation)
        return playing_deck

    def create_shuffled_deck(self):
        playing_deck = self.create_deck()
        random.shuffle(playing_deck)
        return playing_deck


if __name__ == "__main__":
    number_of_decks = 1
    create_deck = CreateDeck(number_of_decks)
    deck = create_deck.create_shuffled_deck()
    print(deck)
