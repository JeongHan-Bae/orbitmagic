import orbitmagic as om

# nombre de cartes
n = 9

# créer un paquet de cartes initial de n cartes
paquet_de_cartes = list(range(1, n + 1))

# ou vous pouvez également utiliser la fonction définie par nous :
paquet0 = om.deck_init(n)

# afficher les cartes
print(paquet_de_cartes)
print(paquet0)

# définir une méthode de mélange
shuffle = [9, 8, 2, 7, 6, 1, 4, 3, 5]

# vérifier si c'est une méthode de mélange disponible qui contient chaque carte d'un paquet
print(om.is_deck(shuffle))

# afficher si un paquet de cartes est le paquet de cartes initial
print(om.is_init(paquet_de_cartes))

# trouver l'orbite de la méthode de mélange
orbite = om.orbit(shuffle)
print(orbite)
# >> 12 : indique que l'application 12 fois de la méthode de mélange renverra à l'état initial

# définir un autre paquet
paquet1 = [4, 5, 8, 7, 9, 6, 3, 1, 2]

# mélanger ce paquet avec la méthode donnée `shuffle`
print(om.shuffle(paquet1, shuffle))
# >> [2, 1, 5, 3, 6, 4, 7, 8, 9]
# les 2 variables doivent être disponibles (examinées avec la fonction `is_pack`) et de même longueur

# calculer le mélange inverse
rev_shuffle = om.reverse(shuffle)
print(rev_shuffle)
# >> [6, 3, 8, 7, 9, 5, 4, 2, 1]

print(om.shuffle(rev_shuffle, shuffle))
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(om.shuffle(shuffle, rev_shuffle))
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mélanger une méthode de mélange avec sa méthode inverse donnera toujours le paquet initial.

equivalent_method_shuffletures = om.cycle(shuffle, 5)
print(equivalent_method_shuffletures)
# >> [9, 3, 8, 7, 6, 1, 4, 2, 5]
# donne le mélange équivalent de mélanger 5 fois la méthode donnée `shuffle`
print(om.rev_cycle(shuffle, -5))
# >> [9, 3, 8, 7, 6, 1, 4, 2, 5]
# inverser la méthode donnée `shuffle` -5 fois (a le même effet que l'opération précédente).

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
     donne toutes les itérations de la méthode `shuffle` donnée jusqu'à ce qu'elle revienne au paquet initial"""

# l'autre paquet
paquet2 = [2, 8, 1, 4, 5, 3, 7, 9, 6]
print(om.find_shuffle(paquet2, paquet1))
# >> [9, 3, 8, 1, 2, 7, 4, 5, 6]
# trouve la méthode de mélange qui peut convertir un paquet en un autre
