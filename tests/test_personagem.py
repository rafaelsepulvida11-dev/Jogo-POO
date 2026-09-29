from src.guerreiro import Guerreiro
from src.inimigo import Inimigo


def test_guerreiro_esta_vivo():

    guerreiro = Guerreiro("Arthur")

    assert guerreiro.esta_vivo() is True


def test_personagem_recebe_dano():
    # TODO
    pass


def test_personagem_morre():
    # TODO
    pass


def test_guerreiro_ataca():
    guerreiro = Guerreiro("Arthur")
    inimigo = Inimigo("Goblin", vida=100, ataque=15, defesa=5)

    guerreiro.atacar(inimigo)

    assert inimigo.vida == 85
