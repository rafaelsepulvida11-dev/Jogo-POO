from guerreiro import Guerreiro
from inimigo import Inimigo
from batalha import Batalha
from item import Item


def main():

    jogador = Guerreiro("Jogador")

    inimigo = Inimigo(
        nome="Goblin",
        vida=100,
        ataque=20,
        defesa=5
    )

    pocao = Item("Poção de cura", 30)
    batalha = Batalha(jogador, inimigo, pocao)

    batalha.iniciar()


if __name__ == "__main__":
    main()
