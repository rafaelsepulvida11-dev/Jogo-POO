from contextlib import redirect_stdout
from io import StringIO

import pygame

from src.arqueiro import Arqueiro
from src.guerreiro import Guerreiro
from src.inimigo import BruxoFinalBoss, Dragao, Goblin
from src.item import PocaoDeVida
from src.mago import Mago


class InterfacePygame:
    LARGURA = 900
    ALTURA = 600

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA))
        pygame.display.set_caption("A Lenda dos Heróis")
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.SysFont("arial", 24)
        self.fonte_pequena = pygame.font.SysFont("arial", 18)
        self.fonte_titulo = pygame.font.SysFont("arial", 40, bold=True)
        self.estado = "selecao"
        self.botoes = []
        self.mensagens = ["Escolha seu herói para iniciar a jornada."]

    def executar(self):
        executando = True
        while executando:
            self._desenhar()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    executando = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        executando = False
                    elif self.estado == "selecao":
                        opcoes = {pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3}
                        if evento.key in opcoes:
                            self._selecionar_personagem(opcoes[evento.key])
                    elif self.estado == "batalha":
                        if pygame.K_1 <= evento.key <= pygame.K_4:
                            self._executar_acao(evento.key - pygame.K_0)
                    elif evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                        self.estado = "selecao"
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    for retangulo, acao in self.botoes:
                        if retangulo.collidepoint(evento.pos):
                            if self.estado == "selecao":
                                self._selecionar_personagem(acao)
                            elif self.estado == "batalha":
                                self._executar_acao(acao)
                            elif self.estado == "resultado":
                                self.estado = "selecao"
                            break
            self.relogio.tick(30)

        pygame.quit()

    def _selecionar_personagem(self, opcao):
        personagens = {
            1: Guerreiro,
            2: Mago,
            3: lambda: Arqueiro("Legolas"),
        }
        self.jogador = personagens[opcao]()
        self.inimigos = [
            Goblin("Goblin"),
            Dragao("Dragão"),
            BruxoFinalBoss("Bruxo Final Boss"),
        ]
        self.indice_inimigo = 0
        self.item = PocaoDeVida(quantidade=3)
        self.estado = "batalha"
        self.mensagens = [f"A jornada de {self.jogador.nome} começa!"]

    def _acoes(self):
        acoes = [(1, "Atacar")]
        if hasattr(self.jogador, "usar_magia"):
            acoes.append((2, "Usar magia"))
            acoes.append((3, f"Poção ({self.item.quantidade})"))
            acoes.append((4, "Fugir"))
        elif hasattr(self.jogador, "atirar_flecha"):
            acoes.append((2, "Atirar flecha"))
            acoes.append((3, f"Poção ({self.item.quantidade})"))
            acoes.append((4, "Fugir"))
        else:
            acoes.append((2, f"Poção ({self.item.quantidade})"))
            acoes.append((3, "Fugir"))
        return acoes

    def _executar_acao(self, opcao):
        inimigo = self.inimigos[self.indice_inimigo]
        acoes = dict(self._acoes())
        if opcao not in acoes:
            return

        if acoes[opcao] == "Fugir":
            self.mensagens = ["Você fugiu da batalha.", "Pressione Enter para continuar."]
            self.resultado = "fuga"
            self.estado = "resultado"
            return

        saida = StringIO()
        with redirect_stdout(saida):
            if opcao == 1:
                self.jogador.atacar(inimigo)
            elif acoes[opcao] == "Usar magia":
                self.jogador.usar_magia(inimigo)
            elif acoes[opcao] == "Atirar flecha":
                self.jogador.atirar_flecha(inimigo)
            else:
                self.item.usar(self.jogador)

            if not acoes[opcao].startswith("Poção") and inimigo.esta_vivo():
                inimigo.realizar_turno(self.jogador)

        self.mensagens = [linha for linha in saida.getvalue().splitlines() if linha][-5:]
        if not self.jogador.esta_vivo():
            self.mensagens = [
                f"{inimigo.nome} venceu a batalha.",
                "Tente novamente e leve seu herói à vitória!",
            ]
            self.resultado = "derrota"
            self.estado = "resultado"
        elif not inimigo.esta_vivo():
            if self.indice_inimigo == len(self.inimigos) - 1:
                self.mensagens = [
                    f"Parabéns, {self.jogador.nome}! Você venceu a campanha!",
                    "Todos os inimigos foram derrotados.",
                ]
                self.resultado = "vitoria"
                self.estado = "resultado"
            else:
                self.indice_inimigo += 1
                self.mensagens.append(
                    f"Próximo inimigo: {self.inimigos[self.indice_inimigo].nome}."
                )

    def _texto(self, texto, posicao, fonte=None, cor=(238, 240, 232)):
        superficie = (fonte or self.fonte).render(texto, True, cor)
        self.tela.blit(superficie, posicao)

    def _barra_vida(self, personagem, posicao, largura):
        x, y = posicao
        pygame.draw.rect(self.tela, (65, 73, 78), (x, y, largura, 18))
        proporcao = max(0, personagem.vida / personagem.vida_maxima)
        pygame.draw.rect(
            self.tela,
            (91, 181, 119),
            (x, y, int(largura * proporcao), 18),
        )
        self._texto(
            f"{personagem.vida}/{personagem.vida_maxima} vida",
            (x, y + 24),
            self.fonte_pequena,
        )

    def _botao(self, texto, acao, retangulo):
        pygame.draw.rect(self.tela, (54, 91, 84), retangulo, border_radius=5)
        pygame.draw.rect(self.tela, (113, 164, 137), retangulo, 2, border_radius=5)
        superficie = self.fonte_pequena.render(texto, True, (248, 247, 235))
        self.tela.blit(superficie, superficie.get_rect(center=retangulo.center))
        self.botoes.append((retangulo, acao))

    def _desenhar(self):
        self.tela.fill((23, 32, 34))
        pygame.draw.rect(self.tela, (34, 46, 46), (32, 28, 836, 544), border_radius=8)
        self._texto("A LENDA DOS HERÓIS", (64, 52), self.fonte_titulo, (232, 191, 105))
        self.botoes = []

        if self.estado == "selecao":
            self._desenhar_selecao()
        elif self.estado == "batalha":
            self._desenhar_batalha()
        else:
            self._desenhar_resultado()

        pygame.display.flip()

    def _desenhar_selecao(self):
        self._texto("Escolha seu personagem", (64, 140), self.fonte)
        descricoes = [
            ("Guerreiro", "Resistente e poderoso"),
            ("Mago", "Domina a magia"),
            ("Arqueiro", "Especialista em flechas"),
        ]
        for indice, (nome, descricao) in enumerate(descricoes, start=1):
            y = 205 + (indice - 1) * 82
            self._texto(f"{indice}  {nome}", (90, y), self.fonte)
            self._texto(descricao, (390, y + 3), self.fonte_pequena, (185, 198, 185))
            self._botao("Escolher", indice, pygame.Rect(690, y - 8, 130, 42))

    def _desenhar_batalha(self):
        inimigo = self.inimigos[self.indice_inimigo]
        self._texto(f"Batalha {self.indice_inimigo + 1}/3", (64, 128), self.fonte_pequena, (185, 198, 185))
        self._texto(self.jogador.nome, (90, 190), self.fonte)
        self._barra_vida(self.jogador, (90, 230), 300)
        if hasattr(self.jogador, "mana"):
            self._texto(f"Mana: {self.jogador.mana}", (90, 280), self.fonte_pequena)
        if hasattr(self.jogador, "flechas"):
            self._texto(f"Flechas: {self.jogador.flechas}", (90, 280), self.fonte_pequena)

        self._texto(inimigo.nome, (510, 190), self.fonte)
        self._barra_vida(inimigo, (510, 230), 300)
        self._texto("Ações", (90, 340), self.fonte)
        for indice, (tecla, nome) in enumerate(self._acoes()):
            coluna = indice % 2
            linha = indice // 2
            self._botao(
                f"{tecla}  {nome}",
                tecla,
                pygame.Rect(90 + coluna * 210, 385 + linha * 58, 190, 44),
            )

        for indice, mensagem in enumerate(self.mensagens[-4:]):
            self._texto(mensagem[:88], (510, 345 + indice * 30), self.fonte_pequena, (215, 211, 184))

    def _desenhar_resultado(self):
        titulos = {
            "vitoria": ("VITÓRIA!", (232, 191, 105)),
            "derrota": ("DERROTA", (220, 105, 95)),
            "fuga": ("BATALHA ENCERRADA", (185, 198, 185)),
        }
        titulo, cor = titulos.get(self.resultado, ("FIM DE JOGO", (238, 240, 232)))
        superficie = self.fonte_titulo.render(titulo, True, cor)
        self.tela.blit(superficie, (90, 155))
        for indice, mensagem in enumerate(self.mensagens):
            self._texto(mensagem[:88], (90, 230 + indice * 42), self.fonte)
        self._botao("Voltar à seleção", 0, pygame.Rect(90, 360, 220, 48))