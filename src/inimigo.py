from src.personagem import Personagem


class Inimigo(Personagem):

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(
            nome=nome,
            vida=vida,
            ataque=ataque,
            defesa=defesa
        )

    def atacar(self, alvo):
        dano = self.ataque
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")
        alvo.receber_dano(dano)
