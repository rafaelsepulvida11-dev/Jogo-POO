from src.arqueiro import Arqueiro
from src.batalha import Batalha
from src.inimigo import BruxoFinalBoss, Dragao, Goblin


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
