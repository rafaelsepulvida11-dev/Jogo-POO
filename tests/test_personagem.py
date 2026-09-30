from src.guerreiro import Guerreiro
from src.inimigo import Inimigo
from src.item import Item
from src.batalha import Batalha


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


def test_inimigo_ataca_jogador():
    inimigo = Inimigo("Goblin", vida=100, ataque=25, defesa=5)
    jogador = Guerreiro("Arthur")

    inimigo.atacar(jogador)

    assert jogador.vida == 110


def test_item_recupera_vida_sem_ultrapassar_o_maximo():
    jogador = Guerreiro("Arthur")
    pocao = Item("Poção de cura", 30)
    jogador.receber_dano(25)

    pocao.usar(jogador)

    assert jogador.vida == jogador.vida_maxima


def test_inimigo_nao_ataca_quando_jogador_usa_item(monkeypatch):
    jogador = Guerreiro("Arthur")
    inimigo = Inimigo("Goblin", vida=100, ataque=25, defesa=5)
    pocao = Item("Poção de cura", 30)
    jogador.receber_dano(25)
    opcoes = iter(["2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(opcoes))

    Batalha(jogador, inimigo, pocao).iniciar()

    assert jogador.vida == jogador.vida_maxima

    pocao.usar(jogador)

    assert jogador.vida == jogador.vida_maxima
