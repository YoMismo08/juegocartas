from baralla import Baralla
from ma import Ma

class Juego:
    def __init__(self):
        self.baralla = Baralla()
        self.baralla.barallar()

    def jugar(self):
        majugador = Ma()

        carta = self.baralla.treure_carta()
        majugador.afegir_carta(carta)
        majugador.mostrar_cartes()
        print("Punts:", majugador.valor)

        while majugador.valor < 21:
            accio = input("Vols una altra carta? (s/n):")
            if accio == "s":
                carta = self.baralla.treure_carta()
                majugador.afegir_carta(carta)
                majugador.mostrar_cartes()
                print("Punts:", majugador.valor)
            else:
                break

        if majugador.valor == 21:
                print("Enhorabona, has guanyat!")
        elif majugador.valor < 21:
                print("T'has plantat a:", majugador.valor)
        else:
                print("Has perdut...")
