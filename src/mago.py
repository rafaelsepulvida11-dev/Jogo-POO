import random

from src.personagem import Personagem


class Mago(Personagem):

    def __init__(self, nome="Merlin"):
        super().__init__(
            nome="Merlin",
            vida=80,
            ataque=30,
            defesa=5
        )

        self.mana = 100

    def atacar(self, alvo):
        dano = self.ataque
        print(f"{self.nome} ataca {alvo.nome} com {dano} de dano.")
        alvo.receber_dano(dano)

    def usar_magia(self, alvo):
        if self.mana < 15:
            print("O mago não possui mana suficiente.")
            return

        self.mana -= 15
        chance = random.randint(1, 10)

        if chance >= 8:
            dano = self.ataque + 50
            print(f"{self.nome} lançou uma magia crítica em {alvo.nome} e causou {dano} de dano!")
        else:
            dano = self.ataque + 25
            print(f"{self.nome} lançou magia em {alvo.nome} e causou {dano} de dano.")

        alvo.receber_dano(dano)

    def mostrar_status(self):
        super().mostrar_status()
        print(f"Mana: {self.mana} | Usos de magia restantes: {self.mana // 15}")
