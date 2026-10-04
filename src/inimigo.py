from src.personagem import Personagem
from src.item import PocaoDeVida


class Inimigo(Personagem):

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(
            nome=nome,
            vida=vida,
            ataque=ataque,
            defesa=defesa
        )
        self.pocao = PocaoDeVida(quantidade=1)

    def atacar(self, alvo):
        print(f"{self.nome} atacou {alvo.nome}!")
        alvo.receber_dano(self.ataque)

    def realizar_turno(self, alvo):
        if self.vida <= self.vida_maxima / 2 and self.pocao.quantidade > 0:
            self.pocao.usar(self)
        else:
            self.atacar(alvo)
        
class BruxoFinalBoss(Inimigo):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=110,
            ataque=25,
            defesa=10
        )
        self.mana = 60

    def atacar(self, alvo):
        # Tenta usar Magia das Sombras se houver mana suficiente, caso contrário usa ataque padrão
        if self.mana >= 20:
            self.magia_das_sombras(alvo)
        else:
            super().atacar(alvo)

    def magia_das_sombras(self, alvo):
        """Ataque especial do Bruxo que consome mana e causa dano extra."""
        custo = 20
        if self.mana < custo:
            print(f"{self.nome} tentou usar Magia das Sombras, mas não possui mana suficiente.")
            return

        self.mana -= custo
        dano = self.ataque + 20
        print(f"{self.nome} usou Magia das Sombras em {alvo.nome}! (Mana restante: {self.mana})")
        alvo.receber_dano(dano)
class Goblin(Inimigo):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=70,
            ataque=15,
            defesa=5
        )

    def atacar(self, alvo):
        # Goblin usa o ataque padrão do Inimigo
        super().atacar(alvo)


class Dragao(Inimigo):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=110,
            ataque=30,
            defesa=0
        )
        self.mana = 30

    def atacar(self, alvo):
        # Tenta usar Bola de Fogo quando há mana suficiente
        if self.mana >= 30:
            self.bola_de_fogo(alvo)
        else:
            super().atacar(alvo)

    def bola_de_fogo(self, alvo):
        """Ataque especial que consome mana e causa grande dano."""
        custo = 30
        if self.mana < custo:
            print(f"{self.nome} tentou usar Bola de Fogo, mas não possui mana suficiente.")
            return

        self.mana -= custo
        dano = self.ataque + 20
        print(f"{self.nome} lançou Bola de Fogo em {alvo.nome}! (Mana restante: {self.mana})")
        alvo.receber_dano(dano)
