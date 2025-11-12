from baralla import Baralla
from ma import Ma

class Juego:
    def __init__(self):
        self.baralla = Baralla()
        self.baralla.barallar()

    def jugar(self):
        majugador = Ma()
        mabot = Ma()

        carta = self.baralla.treure_carta()
        majugador.afegir_carta(carta)
        majugador.mostrar_cartes()
        print("Punts jugador:", majugador.valor)

        cartabot = self.baralla.treure_carta()
        mabot.afegir_carta(cartabot)
        mabot.mostrar_cartes()
        print("Punts bot:", mabot.valor)

        while majugador.valor < 21 and mabot.valor < 21:
            accio = input("Jugador, vols una altra carta? (s/n):")
            if accio == "s":
                carta = self.baralla.treure_carta()
                majugador.afegir_carta(carta)
                majugador.mostrar_cartes()
                print("Punts:", majugador.valor)
                print ("Bot, vols una altra carta?")
                if mabot.valor < 21 or majugador.valor>mabot.valor:
                    print("s")
                    cartabot = self.baralla.treure_carta()
                    mabot.afegir_carta(cartabot)
                    mabot.mostrar_cartes()
                    print("Punts bot:", mabot.valor)
                else:
                    print("n")
            else:
                while majugador.valor == 21 or majugador.valor>mabot.valor:
                        print ("Bot, vols una altra carta?")
                        print("s")
                        cartabot = self.baralla.treure_carta()
                        mabot.afegir_carta(cartabot)
                        mabot.mostrar_cartes()
                        print("Punts bot:", mabot.valor)
                        break
                break

        if majugador.valor == 21:
                print("Enhorabona, has guanyat!")
        elif majugador.valor < 21:
                print("T'has plantat a:", majugador.valor)
        else:
                print("Has perdut...")
