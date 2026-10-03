from src.personagem import Personagem


class Arqueiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=70,
            ataque=40,
            defesa=5
        )

    def atacar(self, alvo):
        print(f"{self.nome} atirou uma flecha em {alvo.nome}!")
        alvo.receber_dano(self.ataque)
