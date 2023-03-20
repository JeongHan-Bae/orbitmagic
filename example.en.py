import orbitmagic as om

# number of cards
n = 9

# create an initial deck of cards of n cards
deck_of_cards = list(range(1, n + 1))

# or you can also use the function defined by us :
my_deck = om.deck_init(n)
# display the cards
print(deck_of_cards)
print(my_deck)

# define a shuffleing method
shuffle = [9, 8, 2, 7, 6, 1, 4, 3, 5]

# verify is that an available shuffleing method which contains each cards of a deck
print(om.is_deck(shuffle))

# display whether a deck of cards is the initial deck of cards
print(om.is_init(deck_of_cards))

# find the orbit of the shuffleing method
orbit = om.orbit(shuffle)
print(orbit)
# >> 12 : indicates that apply 12 times the shuffleing method will return to the initial state

# define another deck
another_deck = [4, 5, 8, 7, 9, 6, 3, 1, 2]
# shuffle that deck with the given method `shuffle`
print(om.shuffle(another_deck, shuffle))
# >> [2, 1, 5, 3, 6, 4, 7, 8, 9]
# all 2 variables should be available (examined with the function `is_deck`) and of the same length

# calculate the reversing shuffle.
rev_shuffle = om.reverse(shuffle)
print(rev_shuffle)
# >> [6, 3, 8, 7, 9, 5, 4, 2, 1]

print(om.shuffle(rev_shuffle, shuffle))
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(om.shuffle(shuffle, rev_shuffle))
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# shuffleing a shuffleing-method with its reverse method will always give the initial deckage.

equivalent_method_shuffletures = om.cycle(shuffle, 5)
print(equivalent_method_shuffletures)
# >> [9, 3, 8, 7, 6, 1, 4, 2, 5]
# gives the equivalent shuffleing of shuffleing 5 times the given method `shuffle`
print(om.rev_cycle(shuffle, -5))
# >> [9, 3, 8, 7, 6, 1, 4, 2, 5]
# reverse the given method `shuffle` -5 times (has the same effect with the previous operation).

print(om.all_cases(shuffle))
""" >>[[9, 8, 2, 7, 6, 1, 4, 3, 5],
     [5, 3, 8, 4, 1, 9, 7, 2, 6],
     [6, 2, 3, 7, 9, 5, 4, 8, 1],
     [1, 8, 2, 4, 5, 6, 7, 3, 9],
     [9, 3, 8, 7, 6, 1, 4, 2, 5],
     [5, 2, 3, 4, 1, 9, 7, 8, 6],
     [6, 8, 2, 7, 9, 5, 4, 3, 1],
     [1, 3, 8, 4, 5, 6, 7, 2, 9],
     [9, 2, 3, 7, 6, 1, 4, 8, 5],
     [5, 8, 2, 4, 1, 9, 7, 3, 6],
     [6, 3, 8, 7, 9, 5, 4, 2, 1],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]]
     gives all the iterations of the given method `shuffle` until it returns to the initial deck"""

# the other deck
the_other_deck = [2, 8, 1, 4, 5, 3, 7, 9, 6]
print(om.find_shuffle(another_deck, the_other_deck))
# >> [9, 3, 8, 1, 2, 7, 4, 5, 6]
# find the shuffleing method that can convert one deck to another
