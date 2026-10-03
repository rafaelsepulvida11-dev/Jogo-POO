from src.guerreiro import Guerreiro
from src.inimigo import Inimigo
from src.mago import Mago
from src.arqueiro import Arqueiro
from src.item import PocaoDeVida


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


def test_goblin_causa_dano_ao_guerreiro():
    guerreiro = Guerreiro("Arthur")
    goblin = Inimigo("Goblin", 70, 20, 5)

    goblin.atacar(guerreiro)

    assert guerreiro.vida == 115


def test_inimigo_usa_pocao_quando_vida_baixa():
    inimigo = Inimigo("Goblin", 100, 30, 5)
    jogador = Guerreiro("Arthur")
    inimigo.vida = 40

    inimigo.realizar_turno(jogador)

    assert inimigo.vida == 60
    assert inimigo.pocao.usado is True
    assert jogador.vida == jogador.vida_maxima


def test_inimigo_ataca_quando_vida_acima_da_metade():
    inimigo = Inimigo("Goblin", 100, 30, 5)
    jogador = Guerreiro("Arthur")
    inimigo.vida = 60

    inimigo.realizar_turno(jogador)

    assert inimigo.vida == 60
    assert jogador.vida == 105


def test_arqueiro_tem_pouca_vida_e_ataca_forte():
    arqueiro = Arqueiro("Legolas")
    inimigo = Inimigo("Goblin", 100, 10, 0)

    arqueiro.atacar(inimigo)

    assert arqueiro.vida == 70
    assert arqueiro.ataque == 40
    assert inimigo.vida == 60


def test_pocao_de_vida_funciona_para_guerreiro_e_arqueiro():
    personagens = [Guerreiro("Arthur"), Arqueiro("Legolas")]

    for personagem in personagens:
        vida_maxima = personagem.vida
        personagem.receber_dano(35)
        PocaoDeVida().usar(personagem)

        assert personagem.vida == min(vida_maxima, vida_maxima - 35 + personagem.defesa + 20)


def test_mago_usa_magia_critica(monkeypatch):
    mago = Mago("Merlin")
    inimigo = Inimigo("Goblin", 50, 10, 0)
    monkeypatch.setattr("random.randint", lambda a, b: 9)
    mago.usar_magia(inimigo)
    assert inimigo.vida < 50
    assert mago.mana < 100
