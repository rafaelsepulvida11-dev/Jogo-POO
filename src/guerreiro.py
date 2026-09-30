from src.personagem import Personagem


class Guerreiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=120,
            ataque=20,
            defesa=15
        )

    def atacar(self, alvo):
        dano = self.ataque
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")
        alvo.receber_dano(dano)
