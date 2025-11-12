class Ma:
    def __init__(self):
        self.cartes = []
        self.valor = 0

    def afegir_carta(self, carta):
        self.cartes.append(carta)
        if carta.valor in ["J", "Q", "K"]:
            self.valor += 10
        elif carta.valor == "As":
            quevols = input("Que vols? 1/11")
            if quevols == "1":
                self.valor += 1
            else:
                self.valor += 11
        else:
            self.valor += int(carta.valor)

    def mostrar_cartes(self):
        for carta in self.cartes:
            print(carta)