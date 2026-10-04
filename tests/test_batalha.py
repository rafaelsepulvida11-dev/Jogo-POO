import src.main as main_module
from src.arqueiro import Arqueiro
from src.batalha import Batalha
from src.inimigo import BruxoFinalBoss, Dragao, Goblin
from src.mago import Mago
from src.guerreiro import Guerreiro


def test_batalha_enfrenta_inimigos_na_ordem(monkeypatch, capsys):
    jogador = Arqueiro("Legolas")
    inimigos = [
        Goblin("Goblin"),
        Dragao("Dragão"),
        BruxoFinalBoss("Bruxo Final Boss"),
    ]
    for inimigo in inimigos:
        inimigo.vida = 1

    monkeypatch.setattr("builtins.input", lambda _: "1")

    Batalha(jogador, inimigos).iniciar()

    saida = capsys.readouterr().out
    posicoes = [
        saida.index("BATALHA CONTRA GOBLIN"),
        saida.index("BATALHA CONTRA DRAGÃO"),
        saida.index("BATALHA CONTRA BRUXO FINAL BOSS"),
    ]
    assert posicoes == sorted(posicoes)
    assert "Legolas venceu todas as batalhas!" in saida


def test_batalha_disponibiliza_ataque_atirar_flecha(monkeypatch, capsys):
    jogador = Arqueiro("Legolas")
    inimigo = Goblin("Goblin")
    inimigo.vida = 50
    monkeypatch.setattr("builtins.input", lambda _: "2")

    Batalha(jogador, [inimigo]).iniciar()

    saida = capsys.readouterr().out
    assert "2 - Atirar flecha" in saida
    assert "atirou uma flecha precisa" in saida
    assert inimigo.vida == 0


def test_fugir_solicita_reinicio_da_partida(monkeypatch):
    jogador = Arqueiro("Legolas")
    inimigo = Goblin("Goblin")
    monkeypatch.setattr("builtins.input", lambda _: "4")

    reiniciar = Batalha(jogador, [inimigo]).iniciar()

    assert reiniciar is True


def test_menu_mostra_quantidade_de_pocoes_do_jogador(monkeypatch, capsys):
    jogador = Arqueiro("Legolas")
    inimigo = Goblin("Goblin")
    monkeypatch.setattr("builtins.input", lambda _: "4")

    batalha = Batalha(jogador, [inimigo])
    assert batalha.item.quantidade == 3
    batalha.iniciar()

    assert "Usar item (Poção de Vida - Quantidade: 3)" in capsys.readouterr().out


def test_main_retorna_a_escolha_de_personagem_apos_fugir(monkeypatch):
    escolhas = iter(["1", "2"])
    batalhas = []

    class BatalhaDeTeste:
        def __init__(self, jogador, inimigos):
            self.jogador = jogador
            self.inimigos = inimigos
            batalhas.append(self)

        def iniciar(self):
            return len(batalhas) == 1

    monkeypatch.setattr("builtins.input", lambda _: next(escolhas))
    monkeypatch.setattr(main_module, "Batalha", BatalhaDeTeste)

    main_module.main()

    assert len(batalhas) == 2
    assert isinstance(batalhas[0].jogador, Guerreiro)
    assert isinstance(batalhas[1].jogador, Mago)
    assert batalhas[0].jogador is not batalhas[1].jogador


def test_main_nao_escolhe_guerreiro_para_entrada_invalida(monkeypatch, capsys):
    escolhas = iter(["", "9", "2"])
    jogadores = []

    class BatalhaDeTeste:
        def __init__(self, jogador, inimigos):
            jogadores.append(jogador)

        def iniciar(self):
            return False

    monkeypatch.setattr("builtins.input", lambda _: next(escolhas))
    monkeypatch.setattr(main_module, "Batalha", BatalhaDeTeste)

    main_module.main()

    saida = capsys.readouterr().out
    assert len(jogadores) == 1
    assert isinstance(jogadores[0], Mago)
    assert "Opção inválida. Escolha 1, 2 ou 3." in saida
    assert "A LENDA DOS HERÓIS" in saida
    assert saida.count("A LENDA DOS HERÓIS") == 3
