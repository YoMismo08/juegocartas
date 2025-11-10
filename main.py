from ma import Ma
from carta import Carta
from baralla import Baralla

baralla = Baralla()
baralla.barallar()

ma = Ma()

carta_treta = baralla.treure_carta()
ma.afegir_carta(carta_treta)
ma.mostrar_cartes()
print("Valor de la ma:", ma.valor)