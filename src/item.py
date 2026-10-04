class Item:

    def __init__(self, nome, valor, quantidade=1):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

    @property
    def usado(self):
        return self.quantidade == 0

    def usar(self, personagem):
        if self.quantidade <= 0:
            print(f"Você não tem mais {self.nome.lower()}.")
            return

        vida_anterior = personagem.vida
        personagem.vida = min(
            personagem.vida + self.valor,
            personagem.vida_maxima
        )

        if personagem.vida == vida_anterior:
            print(f"{personagem.nome} já está com a vida cheia.")
            return

        self.quantidade -= 1
        vida_recuperada = personagem.vida - vida_anterior
        print(
            f"{personagem.nome} usou {self.nome} e recuperou "
            f"{vida_recuperada} de vida! Restam {self.quantidade}."
        )


class PocaoDeVida(Item):
    """Poção que recupera 20 de vida."""

    def __init__(self, quantidade=1):
        super().__init__("Poção de Vida", 20, quantidade)