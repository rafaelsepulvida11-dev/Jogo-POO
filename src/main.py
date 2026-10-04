import os
import sys

if __package__ is None or __package__ == "":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.batalha import Batalha
from src.guerreiro import Guerreiro
from src.inimigo import BruxoFinalBoss, Dragao, Goblin
from src.mago import Mago
from src.arqueiro import Arqueiro


def main():
    while True:
        print("\n" + "=" * 48)
        print("             A LENDA DOS HERÓIS")
        print("=" * 48)
        print("Uma jornada perigosa começa...")
        print("\nEscolha seu personagem:")
        print("  [1] Guerreiro - resistente e poderoso")
        print("  [2] Mago      - domina a magia")
        print("  [3] Arqueiro  - especialista em flechas")
        escolha = input("\nDigite 1, 2 ou 3: ").strip()

        if escolha == "1":
            jogador = Guerreiro()
        elif escolha == "2":
            jogador = Mago()
        elif escolha == "3":
            jogador = Arqueiro("Legolas")
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")
            continue

        inimigos = [
            Goblin("Goblin"),
            Dragao("Dragão"),
            BruxoFinalBoss("Bruxo Final Boss"),
        ]

        batalha = Batalha(jogador, inimigos)
        if not batalha.iniciar():
            break


if __name__ == "__main__":
    main()
