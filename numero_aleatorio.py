# programa para adivinar entre dos jugadores una fruta 
from random import*

#input
X = input( " jugador uno por favor poner el nombre de la fruta a elegir : ")
Y = input( " jugador dos por favor poner el nombre de la fruta a elegir : ")

#processing and ouput 
Z = choice (["manzana" , "pera" , "guanabana" , "guayabas"])

if X == Z and Y == Z:
    print( " los dos jugadores han adivino el nombre de la fruta " , Z ,)
elif X == Z:
    print( " solo el jugador uno ha adivino el nombre de la fruta " , Z ,)
elif Y == Z:
    print( " solo el jugador dos ha adivinado el nombre de la fruta " , Z ,)
else:
    print( " ninguno de los dos ha adivino el nombre de la fruta a elegir " , Z ,)