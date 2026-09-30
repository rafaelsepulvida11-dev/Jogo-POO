import os
import sys

if __package__ is None or __package__ == "":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.batalha import Batalha
from src.guerreiro import Guerreiro
from src.inimigo import Inimigo
from src.mago import Mago


def main():
    print("Escolha a classe do jogador:")
    print("1 - Guerreiro")
    print("2 - Mago")
    escolha = input("Opção: ")

    if escolha == "2":
        jogador = Mago()
    else:
        jogador = Guerreiro()

    inimigo = Inimigo(
        nome="Goblin",
        vida=100,
        ataque=15,
        defesa=5
    )

    batalha = Batalha(jogador, inimigo)
    batalha.iniciar()


if __name__ == "__main__":
    main()
