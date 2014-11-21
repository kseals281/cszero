import collections
import random

"""
Blackjack is a card game where you try to get as close to 21 without going over 
(busting).

Each number card is worth it's value in points. 
Face cards are worth 10 points.
The Ace can either be a 1 or an 11, whichever helps your total more.

You will implement a blackjack player in addition to the actual blackjack game.

There is a lot of extra extra credit available here, but if you just want to do
the basics, just implement the following:
    - Deal
    - Play
    - Player
      * ShouldHit
      * HasBusted
    
Remember: Don't touch any of the code in the restricted section. You shouldn't
alter the Game, the Dealer, or any of the variables defined in there.

Extra Extra Credit
    - Allow the game to play with more than one deck.
      Use the following prompt: 'Enter the number of decks: '
    - Keep track of money. There is an Account instance associated with each
      player. For the basic implementation, you can ignore that. But for extra
      extra credit, you can keep track of how much money each player has in the
      account. So you'll have to support making a bet (assume for each game, a
      player will bet $1). If the player wins, he earns $1 extra dollar. If he
      loses, he loses his $1. If the dealer and player tie, player gets his 
      money back.
    - Double down support. If you support keeping track of money, you can
      support doubling down. That means that a player can double their bet in 
      exchange for taking exactly one more card. This means if they decide that
      they should double down (in other words, if ShouldDoubleDown returns True)
      then the player's bet will be doubled and he can only get hit one more
      time.
    - Let it ride. Add support for letting it ride. 
    - If you are dealt two cards of the same value, you can split the cards.
      The result of splitting the deck is as follows:
      * Create another player and add him to the game. The new player should use
        the existing player's Account instance.
      * The player that split loses one card and the new player gets that card
        (so now each player has one card).
      * Deal the old player and then the new player a new card so that they now
        each have 2 cards.
        Note: a person cannot split twice in the same round.
      * When the round is over, the additional player gets removed from the game
        (so at the end of each round, the total number of players is the same as
        it was at the beginning of the round).
      * If you split, you have to place a bet for the new player, too (if you 
        are supporting taking bets). Meaning, if you only have $1 left in your 
        account at the beginning of the game, you won't be able to split because
        you already bet your $1 dollar.
"""
############################ DO NOT TOUCH THIS CODE ############################

DIAMONDS = 'diamonds'
CLUBS = 'clubs'
HEARTS = 'hearts'
SPADES = 'spades'
SUITS = [DIAMONDS, CLUBS, HEARTS, SPADES]

JACK = 'jack'
KING = 'king'
QUEEN = 'queen'
ACE = 'ace'
FACE_VALUES = [JACK, QUEEN, KING]

STARTING_BALANCE = 100


def GenerateCardValues():
    """Creates a dictionary mapping the card's string name to its values."""
    values = collections.OrderedDict()
    for i in xrange(2, 11):
        values[str(i)] = [i]
    for face in FACE_VALUES:
        values[face] = [10]
    values[ACE] = [1, 11]
    return values


def GetCardValue(card):
    """Gets the value(s) of the given card as a list of integers.

    For example, ('ace', 'hearts') will return [1, 11].
                 ('2', 'diamonds') will return [2]. 
    """
    return GenerateCardValues()[card[0]]



def GenerateDeck():
    """Creates a sorted deck of 52 cards."""
    deck = []
    for suit in SUITS:
        for key in GenerateCardValues():
            deck.append((key, suit))
    return deck

    
def Shuffle(cards):
    """Does an in-place shuffle of the provided cards."""
    return random.shuffle(cards)
    

def GetPossibleTotals(cards):
    """Returns a list containing all of the possible values for a set of cards.
    
    Normally, the total will just be the sum of all of the values of the cards
    in the hand as a one-item list (e.g. if the cards are a 10 and a 2, then
    this will return [12]).
    
    When the hand contains at least one Ace, then you end up with multiple 
    possible totals for the hand because Aces have 2 different values. So for
    example, if the cards are Ace and 10, then you will get back [11, 21].
    """
    if len(cards) == 0:
        return 0
    card_values = GenerateCardValues()
    totals = card_values[cards[0][0]][:]
    if len(cards) == 1:
        return totals
    for card in cards[1:]:
        for total in totals[:]:
            totals.remove(total)
            v = card_values[card[0]]
            for val in v:
                totals.append(val + total)
    return totals


class Account(object):
    def __init__(self, balance):
        self.balance = balance
        
################################################################################

class Player(object):
    
    def __init__(self, account):
        self.cards = []
        self.account = account
        
    def ShouldHit(self, game):
        """Determines whether or not a player should hit.
    
        This is where you create a smart player--try to be smarter than the 
        dealer. 
        
        This should return False if the player has busted.
        
        Once you decide to stay in a game, you must always stay until that game
        is over. You can't change your mind and then hit again.
        
        You may use random behavior here (the random module has been imported).
        However, again, once you decide to stay once, you're done with the game.
        
        The game parameter is an instance of a Game. This gives you access to
        the dealer and players' cards. Knowing what other people have may help
        you to create a better, smarter player.
        """
        # You haven't learned classes, so here's how you can use a couple of
        # values.
        total = GetPossibleTotals(self.cards)
        if self.HasBusted(self.cards) == True:
			return False
        if 21 in total:
			return False
        elif len(total) == 1 and (20 in total or 19 in total or 18 in total):
			return False
        elif len(total) > 1 and total[0] > 17:
			return False
        else:
            return True
		#print self.cards  # prints out the player's cards
        #print game.dealer.cards  # prints out the dealer's cards
        
    def ShouldDoubleDown(self, game):
        """This function is ignored unless you implement and use it.
        
        Returns True if you want to double-down, False otherwise.
        
        Remember, if you double-down, you only get to get hit one more time.
        """
        return False
        
    def HasBusted(self, cards):
        """Tells if a player has busted or not.
    
        If there is no way that the player's hand can add up to anything less 
        than 22, then the player has busted. 
    
        Return True if the player has busted; return False otherwise.
        """
        total = GetPossibleTotals(self.cards)
        if total[0] > 21:
			return True
        else:
			return False
    
############################ DO NOT TOUCH THIS CODE ############################

class Dealer(Player):
    
    def __init__(self):
        super(Dealer, self).__init__(None)
        
    # This will use your implementation of HasBusted, that's why you don't see 
    # it implemented here.
    def ShouldHit(self, game):
        """Determines whether or not dealer should hit.
        
        This dealer will hold at a hard 17. If he possibly has a value less than
        17, then the dealer will hit. For example, if he has Ace and 6, he will
        hit because that can be viewed as 7. 
        """
        totals = GetPossibleTotals(self.cards)
        for total in totals:
            if total <= 17:
                return True
        return False
    
    def ShouldDoubleDown(self, game):
        return False


class Game(object):
    """The Game class contains all of the players and the dealer."""
    def __init__(self, num_players):
        self.dealer = Dealer()
        self.players = []
        for i in xrange(num_players):
            account = Account(STARTING_BALANCE)
            self.players.append(Player(account))

################################################################################

def Deal(cards, game):
    """When dealing cards, you must follow the steps described:
        - Shuffle the deck
        - One card goes to each player (starting at player 0)
        - The second card goes to each player
        - The dealer gets 2 cards 
    """
    Shuffle(cards)
    for i in xrange(2):
		for x in xrange(len(game.players)):
			(game.players[x]).cards.append(cards.pop(0))
    game.dealer.cards.append(cards.pop(0))
    game.dealer.cards.append(cards.pop(0))
		


def Play(cards, num_players):
    """Play a game of blackjack.
    
    To play a game, do the following things:
        - Create an instance of a Game (done for you)
        - Deal the cards (done for you)
        - Rotate through each player and have him decide what to do.
          * If the player says True to ShouldHit, then give him another card.
          * If the player says False to ShouldHit, then that player is done.
        - Keep rotating through the players until everyone has either stayed
          or busted (HasBusted is True and ShouldHit is False)
        - If a player or dealer says ShouldHit, then the game must hit. Same
          with ShouldDoubleDown (if the player says he should do something,
          that thing should be done).
    """
    game = Game(num_players)
    cards = GenerateDeck()
    Deal(cards, game)
    final = []
    for i in xrange(len(game.players)):
		while len(game.players) >= i:
			decision = Player.ShouldHit(game.players[i], game)
			print 'Player', i + 1, '\b\'s cards are: ', game.players[i].cards
			print 'Their possible card total(s):', GetPossibleTotals(game.players[i].cards)
			if decision == True:
				if len(game.players[i].cards) == 5:
					print 'They got 5 cards and did not bust\n\n'
					final.append(21)
					break
				print 'They have decided to hit'
				game.players[i].cards.append(cards.pop(0))
				pause = raw_input('Press any key to continue....\n\n')
			elif decision == False and game.players[i].HasBusted(game.players[i].cards) == False:
				for o in xrange(len(GetPossibleTotals(game.players[i].cards))):
					if (GetPossibleTotals(game.players[i].cards))[o] > 21:
						o -= 1
						break
				final.append((GetPossibleTotals(game.players[i].cards))[o])
				print 'They have decided to stay'
				pause = raw_input('Press any key to continue....\n\n')
				break
			else:
				final.append((GetPossibleTotals(game.players[i].cards))[0])
				print 'They have busted'
				pause = raw_input('Press any key to continue....\n\n')
				break
		print 'Current scoreboard:', final
    while Dealer.ShouldHit(game.dealer, game) == True and 21 not in GetPossibleTotals(game.dealer.cards) and game.dealer.HasBusted(game.dealer.cards) == False:
		if min(final) > 21:
			break
		print 'The Dealer\'s cards are:', game.dealer.cards
		print 'His possible total(s):', GetPossibleTotals(game.dealer.cards)
		game.dealer.cards.append(cards.pop(0))
		pause = raw_input('Press any key to continue....\n\n')
    print 'The Dealer\'s cards are:', game.dealer.cards
    print 'His final total(s):', GetPossibleTotals(game.dealer.cards)
    pause = raw_input('Press any key to continue....\n\n')
    for o in xrange(len(GetPossibleTotals(game.dealer.cards))):
	    if game.dealer.cards[o] > 21:
			o -= 1
			break
    final.append((GetPossibleTotals(game.dealer.cards))[o])
    print final
    winner = 0
    tie = []
    for i in xrange(len(final)):
		if final[i] <= 21 and final[i] > winner:
			winner = final[i]
			del tie[:]
			tie.append(i + 1)
		elif final[i] <= 21 and final[i] == winner:
			tie.append(i + 1)
    if len(tie) > 1:
		print '\n\nThe winners are', tie, 'with the score of', winner
    elif winner == 0:
		print '\n\nEveryone busted. The house wins'
    elif final.index(winner) == (len(final) - 1):
		print '\n\nThe winner is the Dealer with a score of', winner
    else:
		print '\n\nThe winner is Player', final.index(winner) + 1, 'with a score of', winner

			
# Add the rest of your Play implementation here.
   
Play(GenerateDeck(), 3)
