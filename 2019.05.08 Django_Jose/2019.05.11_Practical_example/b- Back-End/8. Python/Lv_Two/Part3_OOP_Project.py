#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
# SUITE = 'H D S C'.split()
# RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# I move the aobve lists in to Deck class
class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        deck=[]
        SUITE = 'H D S C'.split()
        RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
        for x in RANKS:
            for y in SUITE:
                item = [x+y]
                deck += item
        shuffle(deck)
        self.deck=[deck[0:26],deck[26:]]
class Hand:
    """
    I moved All the method and function in this class in to the Player class
    """
    pass

class Player:
    '''
    This is from the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    name=""
    cards=[]
    def add(self,cards):
        self.cards += cards
    def remove(self):
        a = self.cards.pop(0)
        return a
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def check(self):
        if len(self.cards)==0:
            return True
        else:
            return False


# Fucntion to care score of 2 cards
def compare(a,b):
    a = list(a)[0]
    b = list(b)[0]
    # A fucntion to cal Score
    def score(a):
        if( a == 'J'):
            a_score = 11
        elif( a == 'Q'):
            a_score = 12
        elif( a == 'K'):
            a_score = 13
        elif( a == 'A'):
            a_score = 14
        else:
            a_score = int(a)
        return a_score
    # Score for a
    a_score= score(a)
    # Score for b
    b_score = score(b)

    # Compare:

    if a_score > b_score:
        return 'Player'
    elif a_score == b_score:
        return 'Same'
    else:
        return 'Computer'




######################
#### GAME PLAY #######
######################

#First, welcome our 2 create 2 players

print("Welcome to War, let's begin...")
player=Player()
computer=Player()
computer.name ='Computer'
player.name = input("Hi, player 1, what's your name?")
print("\n")

while True:

    # Show
    deck = Deck()
    player.cards = deck.deck[0]
    computer.cards = deck.deck[1]
    print(f"{player.name}, your cards are: {player.cards} ")
    print("\n")
    table =[]
    turn = 0
    while True:
        input('Press any key to continue')
        print("\n")
        print(f'Turn {turn} starts')
        print("\n")
        # Table includes 2 list. The first one is Player's war card. The second one is Computer's war cards
        table = [[player.remove()],[computer.remove()]]
        print(f" player1 have {table[0]}, computer have {table[1]}")
        print("\n")


        # First time "Same"
                    #First list's last item   ,  #Second list's last Item
        if compare(table[0][len(table[0])-1],table[1][len(table[1])-1]) == "Same":
            print('PLayer and Computer have the same score, we have 6 more cards on the war table')
            print("\n")
            input('Press any key to continue')
            print("\n")
            table[0] += [player.remove()] + [player.remove()]+ [player.remove()]
            table[1] += [computer.remove()] + [computer.remove()] + [computer.remove()]
            print(f" player1 have {table[0]}, computer have {table[1]}")
            print("\n")

            # The second and beyond of "Same"
            while compare(table[0][len(table[0])-1],table[1][len(table[1])-1]) =="Same":
                if player.check() or computer.check():
                    break
                print('PLayer and Computer have the same score once again, we need 2 more cards on the war table')
                print("\n")
                input('Press any key to continue')
                print("\n")
                table[0] += [player.remove()]
                table[1] += [computer.remove()]
                print(f" player1 have {table[0]}, computer have {table[1]}")
                print("\n")

            # Whenever the reuls of compare is not Same. This happen.
            else:
                if compare(table[0][len(table[0])-1],table[1][len(table[1])-1]) =="Player":
                    print(f"{player.name} win this round. Player take all the cards {table[0]} and {table[1]}")
                    print("\n")
                    player.add(table[0])
                    player.add(table[1])
                else:
                    print(f"Computer win this round. Computer take all the cards {table[0]} and {table[1]}")
                    print("\n")
                    computer.add(table[0])
                    computer.add(table[1])
                if input("Do you want to continue this game? Y/N") == "N":
                    break

        # If there isn't any Same: from the Beginning
        else:
            if compare(table[0][len(table[0])-1],table[1][len(table[1])-1]) == "Player":
                print(f"{player.name} win this round. Player take all the cards {table[0]} and {table[1]}")
                print("\n")
                player.add(table[0])
                player.add(table[1])
            else:
                print(f"Computer win this round. Computer take all the cards {table[0]} and {table[1]}")
                print("\n")
                computer.add(table[0])
                computer.add(table[1])
            if input("Do you want to continue this game? Y/N") == "N":
                break
        print(f"Your cards are now: {player.cards}")
        print("\n")
        if player.check():
            print("Unfortunately, Computer has won. ")
            print("\n")
            break
        if computer.check():
            print("Congratualation, You has won. ")
            print("\n")
            break
        turn +=1

    if input("Do you want to play one more game ?, Please answer Y/N").lower()=="Y":
        print("\n")
        continue
    else:
        print(f"Thank you for enjoying our game. We hope to see you again, {player.name}")
        print("\n")
        break











# Use the 3 classes along with some logic to play a game of war!
