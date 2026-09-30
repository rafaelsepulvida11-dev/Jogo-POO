class Item:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def usar(self, personagem):
        # TODO: implementar efeito do item
        pass
class PocaoDeVida(Item):
    """Poção que recupera 20 de vida."""

    def __init__(self):
        super().__init__("Poção de Vida", 20)