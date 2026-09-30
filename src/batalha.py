class Batalha:

    def __init__(self, jogador, inimigo, item):
        self.jogador = jogador
        self.inimigo = inimigo
        self.item = item

    def iniciar(self):

        print("=" * 40)
        print("        INÍCIO DA BATALHA")
        print("=" * 40)

        while self.jogador.esta_vivo() and self.inimigo.esta_vivo():

            print("\n--- STATUS ---")
            self.jogador.mostrar_status()
            self.inimigo.mostrar_status()

            print("\n--- AÇÕES ---")
            print("1 - Atacar")
            print("2 - Usar item")
            print("3 - Fugir")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.jogador.atacar(self.inimigo)
                if self.inimigo.esta_vivo():
                    self.inimigo.atacar(self.jogador)

            elif opcao == "2":
                self.item.usar(self.jogador)

            elif opcao == "3":
                print("Você fugiu da batalha!")
                return

            else:
                print("Opção inválida.")
                continue

        # TODO: verificar quem venceu
