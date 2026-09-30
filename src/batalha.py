class Batalha:

    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

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
            print("2 - Usar magia")
            print("3 - Usar item")
            print("4 - Fugir")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.jogador.atacar(self.inimigo)
            elif opcao == "2":
                if hasattr(self.jogador, "usar_magia"):
                    self.jogador.usar_magia(self.inimigo)
                else:
                    print("Seu personagem não sabe usar magia.")
            elif opcao == "3":
                print("Você usou um item, mas não há item implementado ainda.")
            elif opcao == "4":
                print("Você fugiu da batalha!")
                return
            else:
                print("Opção inválida.")
                continue

            if not self.inimigo.esta_vivo():
                break

            self.inimigo.atacar(self.jogador)

        if self.jogador.esta_vivo():
            print(f"\n{self.jogador.nome} venceu a batalha!")
        else:
            print(f"\n{self.inimigo.nome} venceu a batalha!")
