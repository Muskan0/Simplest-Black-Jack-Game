import random
suits=('Hearts','Diamonds','Spades','Club')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Jack':10,'King':10,'Queen':10,'Ace':11}
playing= True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+' of '+self.suit

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffler(self):
        random.shuffle(self.deck)
    def deals(self):
        single_card=self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank] ###
        if card.rank=='Ace':
            self.aces+=1

    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1 ###

class Chips:
    def __init__(self):
        self.total=100
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet =int(input('Enter the bet amount'))
        except:
            print('Pass an integer value')
        else:
            if chips.bet>chips.total:
                print('you do not have enough number of chips, you have: {}'.format(chips.total))
            else:
                break

def hit(decks,hand):
    single_card=decks.deals()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(decks,hand):
    global playing
    while True:
        a=input(print("Do you want to hit or stand?"))
        if a=='hit':
            hit(decks,hand)
        elif a=='stand':
            print("Player stands, dealer's turn")
            playing=False
        else:
            print("I didn't understand.Enter 'hit' or 'stand' only")
            continue
        break

def show_some(player,dealer):
    print("Dealer's hand:")
    print("Dealer's one card hidden!")
    print(dealer.cards[1])
    print('\n')
    print("Player's hand:")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("Player's hand:")
    for card in player.cards:
        print(card)

def player_busts(chips):
   print('Player busts! Dealer wins')
   chips.lose_bet()
def dealer_busts(chips):
    print('Dealer busts! Player wins')
    chips.win_bet()
def player_wins(chips):
    print('Player wins')
    chips.win_bet()
def dealer_wins(chips):
    print('dealer wins')
    chips.lose_bet()
def push():
    print('Dealer and player tie!')

while True:
    print("WELCOME TO THE BLACK JACK GAME")
    #Create and shuffle the deck, deal two cards to each player
    deck=Deck()
    deck.shuffler()
    player_hand= Hand()
    player_hand.add_card(deck.deals())
    player_hand.add_card(deck.deals())
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deals())
    dealer_hand.add_card(deck.deals())
    player_chips=Chips()
    print("We are providing you with a chip total of 100")
    take_bet(player_chips)
    show_some(player_hand, dealer_hand)
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value>21:
            player_busts(player_chips)
            break
    if player_hand.value<=21:
        while dealer_hand.value<17:
            hit(deck,dealer_hand)
        print('\n\nAll the cards are:')
        show_all(player_hand,dealer_hand)
        if dealer_hand.value>21:
            dealer_busts(player_chips)
        elif player_hand.value>dealer_hand.value:
            player_wins(player_chips)
        elif player_hand.value<dealer_hand.value:
            dealer_wins(player_chips)
        else:
            push()
    print(f"Player, your chips total is: {player_chips.total}")
    if input('Do you want to play again?(y/n)')=='y':
        playing=True
        continue
    else:
        print('Thank you for playing.')
        break
