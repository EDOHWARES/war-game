import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7, 
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    


class Deck:
    def __init__(self) -> None:
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
    
    def empty_deck(self):
        while len(self.all_cards) >= 1:
            self.deal_one()



class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.all_cards)} cards"
    


# GAME SETUP
    
# Instantiate both players
player1 = Player("One")
player2 = Player("Two")

# Instantiate new deck and shuffle
newDeck = Deck()
newDeck.shuffle()

# Sharing the deck cards equally for both players
for x in range(26):
    player1.add_cards(newDeck.deal_one())
    player2.add_cards(newDeck.deal_one())

game_on = True

round = 0

while game_on:
    round += 1
    print(f"Round: {round}")

    # Checking if any of the Player is out of cards, so as to stop the game
    if len(player1.all_cards) == 0:
        print("Player One is out of Cards!, Player Two Wins!")
        game_on = False
        break
    elif len(player2.all_cards) == 0:
        print("Player Two is out of Cards!, Player One Wins!")
        game_on = False
        break
    else:
        pass

    # Playing cards to the table
    player1_played_cards = []
    player1_played_cards.append(player1.remove_one())

    player2_played_cards = []
    player2_played_cards.append(player2.remove_one())

    at_war = True

    while at_war:
        if player1_played_cards[-1].value > player2_played_cards[-1].value:
            player1.add_cards(player1_played_cards)
            player1.add_cards(player2_played_cards)
            at_war = False
        elif player2_played_cards[-1].value < player2_played_cards[-1].value:
            player2.add_cards(player1_played_cards)
            player2.add_cards(player2_played_cards)
            at_war = False
        else:
            print("WAR!")

            if len(player1.all_cards) < 5:
                print("Player One unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break
            elif len(player2.all_cards) < 5:
                print("Player Two unable to declare war")
                print("PLAYER ONE WINS!")
                game_on = False
                break
            else:
                for num in range(5):
                    player1_played_cards.append(player1.remove_one())
                    player2_played_cards.append(player2.remove_one())




    


