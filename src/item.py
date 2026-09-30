class Item:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.usado = False

    def usar(self, personagem):
        if self.usado:
            print(f"{self.nome} já foi usado.")
            return

        vida_anterior = personagem.vida
        personagem.vida = min(
            personagem.vida + self.valor,
            personagem.vida_maxima
        )

        if personagem.vida == vida_anterior:
            print(f"{personagem.nome} já está com a vida cheia.")
            return

        self.usado = True
        vida_recuperada = personagem.vida - vida_anterior
        print(
            f"{personagem.nome} usou {self.nome} e recuperou "
            f"{vida_recuperada} de vida!"
        )
class PocaoDeVida(Item):
    """Poção que recupera 20 de vida."""

    def __init__(self):
        super().__init__("Poção de Vida", 20)