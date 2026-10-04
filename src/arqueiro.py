from src.personagem import Personagem


class Arqueiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=70,
            ataque=25,
            defesa=15
        )
        self.flechas = 10

    def atacar(self, alvo):
        if not self._usar_flecha():
            return

        print(f"{self.nome} atirou uma flecha em {alvo.nome}!")
        alvo.receber_dano(self.ataque)

    def atirar_flecha(self, alvo):
        if not self._usar_flecha():
            return

        dano = self.ataque + 35
        print(f"{self.nome} atirou uma flecha precisa em {alvo.nome}, causando {dano} de dano!")
        alvo.receber_dano(dano)

    def _usar_flecha(self):
        if self.flechas <= 0:
            print(f"{self.nome} não possui flechas.")
            return False

        self.flechas -= 1
        return True

    def mostrar_status(self):
        super().mostrar_status()
        print(f"Flechas: {self.flechas}")
