from src.guerreiro import Guerreiro
from src.inimigo import Inimigo
from src.mago import Mago


def test_guerreiro_esta_vivo():
    guerreiro = Guerreiro("Arthur")
    assert guerreiro.esta_vivo() is True


def test_personagem_recebe_dano():
    inimigo = Inimigo("Goblin", 50, 10, 5)
    inimigo.receber_dano(20)
    assert inimigo.vida == 35


def test_personagem_morre():
    inimigo = Inimigo("Goblin", 10, 10, 0)
    inimigo.receber_dano(30)
    assert inimigo.esta_vivo() is False


def test_guerreiro_ataca():
    guerreiro = Guerreiro("Arthur")
    inimigo = Inimigo("Goblin", 50, 10, 0)
    guerreiro.atacar(inimigo)
    assert inimigo.vida < 50


def test_mago_usa_magia_critica(monkeypatch):
    mago = Mago("Merlin")
    inimigo = Inimigo("Goblin", 50, 10, 0)
    monkeypatch.setattr("random.randint", lambda a, b: 9)
    mago.usar_magia(inimigo)
    assert inimigo.vida < 50
    assert mago.mana < 100
