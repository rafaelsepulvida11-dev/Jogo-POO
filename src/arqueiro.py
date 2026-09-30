from personagem import Personagem


class Arqueiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=150,
            ataque=20,
            defesa=15
        )

    def atacar(self, alvo):
        print(f"{self.nome} atirou uma flecha em {alvo.nome}!")
        alvo.receber_dano(self.ataque)
