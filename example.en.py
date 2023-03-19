import orbitmagic as om

# number of cards
n = 9

# create an initial pack of cards of n cards
pack_of_cards = list(range(1, n + 1))

# or you can also use the function defined by us :
my_pack = om.pack_init(n)
# display the cards
print(pack_of_cards)
print(my_pack)

# define a mixing method
mix = [9, 8, 2, 7, 6, 1, 4, 3, 5]

# verify is that an available mixing method which contains each cards of a pack
print(om.is_pack(mix))

# display whether a pack of cards is the initial pack of cards
print(om.is_init(pack_of_cards))

# find the orbit of the mixing method
orbit = om.orbit(mix)
print(orbit)
# >> 12 : indicates that apply 12 times the mixing method will return to the initial state

# define another pack
another_pack = [4, 5, 8, 7, 9, 6, 3, 1, 2]
# mix that pack with the given method `mix`
print(om.mix(another_pack, mix))
# >> [2, 1, 5, 3, 6, 4, 7, 8, 9]
# all 2 variables should be available (examined with the function `is_pack`) and of the same length

# calculate the reversing mix.
rev_mix = om.reverse(mix)
print(rev_mix)
# >> [6, 3, 8, 7, 9, 5, 4, 2, 1]

print(om.mix(rev_mix, mix))
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(om.mix(mix, rev_mix))
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mixing a mixing-method with its reverse method will always give the initial package.

equivalent_method_mixtures = om.cycle(mix, 5)
print(equivalent_method_mixtures)
# >> [9, 3, 8, 7, 6, 1, 4, 2, 5]
# gives the equivalent mixing of mixing 5 times the given method `mix`
print(om.rev_cycle(mix, -5))
# >> [9, 3, 8, 7, 6, 1, 4, 2, 5]
# reverse the given method `mix` -5 times (has the same effect with the previous operation).

print(om.all_cases(mix))
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
     gives all the iterations of the given method `mix` until it returns to the initial pack"""

# the other pack
the_other_pack = [2, 8, 1, 4, 5, 3, 7, 9, 6]
print(om.find_mix(another_pack, the_other_pack))
# >> [9, 3, 8, 1, 2, 7, 4, 5, 6]
# find the mixing method that can convert one pack to another
