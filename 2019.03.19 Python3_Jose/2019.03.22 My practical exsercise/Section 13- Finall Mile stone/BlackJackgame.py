# So we have a player and the dealer
# we have only rule for blackjack, win, lose, first round surrender.
# so we have the class Deck. The Deck will have auto create cards,shuffle and give card.
# we have parent class BlackJack with attributes: score, cards. Method takecard(), scorecal().
# subclass player will have another attribute: bet_amount.

# Create the Deck() class
from random import shuffle
class Deck():
    def __init__(self):
        RANKS=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        SUITES=['H','D','S','C']
        cards=[]
        for rank in RANKS:
            for suite in SUITES:
                cards += [rank+suite]
        self.cards=cards

    def givecard(self):
        shuffle(self.cards)
        return self.cards.pop(0)

# Create Parrent BlackJack class:
class BlackJack():
    score=0
    cards=[]

    def takecard(self,card):
        self.cards+=card

    def scorecal(self):
        #Black Jack case
        if len(self.cards) ==2 and (self.cards[0] =='A' or self.cards[1] =='A'):
            if self.cards[0] =='A' and self.cards[1] =='A':
                return "AA Black Jack"
            else:
                return "Black Jack"
        #Cal score for non A card
        else:
            for card in self.cards:
                if card[0] == 'J':
                    self.score += 11
                if card[0] == 'Q':
                    self.score += 12
                if card[0] == 'K':
                    self.score += 13
                if card[0] == 'A':
                    pass
                else:
                    self.score += int(card[0])
        #Cal score for  Acard
            for card in self.cards:
                if card[0] == 'A':
                    if self.score <= 10:
                        self.score += 11
                    elif self.score == 11:
                        self.score += 10
                    elif self.score >= 11:
                        self.score += 1
        return self.score

#class player(BlackJack)

class Player(BlackJack):
    name=''
    score=5000
    bet_amount=0

class Dealer(BlackJack):
    score = 10000

#A Function to campare score:

def compare(a,b):
    if a == b:
        return 'Equal'
    elif a > 21 and b >21:
        if a < b:  return "Win"
        else:   return "Lose"
    elif a > 21: return "Lose"
    elif b >21: return "Win"

    elif a == 'AA Black Jack' and b == 'Black Jack':
        return "Win"
    elif b == 'AA Black Jack' and a == 'Black Jack':
        return "Lose"
    elif a > b:
        return "Win"
    elif a < b:
        return "Lose"

# Game play:

while True: #Level one loop
    player=Player()
    dealer= Dealer()
    player.name =input("Welcome to the Black Jack game. Player, may I know your name? \n Input your name here: ")
    deck = Deck()
    while True: #Level two loop

        turn = 0
        while True: #A separated loop, don't need to be kept track on.
            player.bet_amount = int(input("How much do you want to bet? Please input an interger"))
            if player.bet_amount <= player.score and player.bet_amount <= dealer.score :
                break #The bet amount is ok
            else:
                print("Your bet is excess your score/dealer's score, please place the bet amount again")
                print(f"Your score is {player.score}, dealer's score is {dealer.score}"")
                continue #Give the bet again
        dealer.takecard(deck.givecard())
        dealer.takecard(deck.givecard())
        player.takecard(deck.givecard())

        while True: # Level three loop

            player.takecard(deck.givecard())

            print("Your cards are: "+player.cards + "\nYour score is "+player.scorecal())
            print("Dealer's first card is "+dealer.cards[0])

            #surrender:
            if dealer.cards[0][0] == 'A' and (turn == 0 or turn == 1):
                surrender = lower(input("Do you want to surrender ? (Y/N)"))
                if surrender == 'Y':
                    player.score -= player.bet_amount/2
                    dealer.score += player.bet_amount/2
                    break #Return to level two loop.
                else:
                    pass
            if player.scorecal() >= 22:
                print("Oh, you have excess the limit")
                break #Return to level two loop.
            elif player.scorecal() >=17:
                if input('Do you want to stop taking cards? (Y/N)') ==Y:
                    break #Return to level two loop.
                else:
                    pass
            input("You are receiving another card, press any key to continue")
            continue #continue this level three loop

        #Check surrender
        if surrender == "Y":
            if input("Do you want to play another round? (Y/N)") =='Y':
            print("Dealer's cards are "+dealer.cards)
            input('\nPress any key to continue')
                continue #continue to the level two loop. Skip the
        else:
            pass

        # No surrender, Dealer take cards:
        while dealer.scorecal() <= 16 and dealer.scorecal()!= "AA Black Jack" and dealer.scorecal() != "Black Jack" :
            dealer.takecard(deck.givecard())
            #done ? Rediculous fast, man :))

        #Compare score and

        #Works left: 1/ win, lose. 2/ Conditional check for player/ dealer score (> 0).

        if compare(player.scorecal(),dealer.scorecal()) =='Win':
            player.score += player.bet_amount
            dealer.score -= player.bet_amount
            print('Congratualation, you have win, your score is now +'+player.bet_amount + ' = ' + player.score)

        elif compare(player.scorecal(),dealer.scorecal()) =='Lose':
            pass
        elif compare(player.scorecal(),dealer.scorecal()) =='Equal':
            pass
