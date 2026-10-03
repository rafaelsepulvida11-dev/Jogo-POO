from src.item import PocaoDeVida


class Batalha:

    def __init__(self, jogador, inimigos):
        self.jogador = jogador
        self.inimigos = inimigos
        self.item = PocaoDeVida()

    def iniciar(self):

        print("=" * 40)
        print("        INÍCIO DA CAMPANHA")
        print("=" * 40)

        for inimigo in self.inimigos:
            if not self.jogador.esta_vivo():
                break

            print(f"\n--- BATALHA CONTRA {inimigo.nome.upper()} ---")
            while self.jogador.esta_vivo() and inimigo.esta_vivo():
                print("\n--- STATUS ---")
                self.jogador.mostrar_status()
                inimigo.mostrar_status()

                print("\n--- AÇÕES ---")
                print("1 - Atacar")

                if hasattr(self.jogador, "usar_magia"):
                    print("2 - Usar magia")
                    print("3 - Usar item")
                    print("4 - Fugir")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        self.jogador.atacar(inimigo)
                        if inimigo.esta_vivo():
                            inimigo.realizar_turno(self.jogador)
                    elif opcao == "2":
                        self.jogador.usar_magia(inimigo)
                        if inimigo.esta_vivo():
                            inimigo.realizar_turno(self.jogador)
                    elif opcao == "3":
                        self.item.usar(self.jogador)
                    elif opcao == "4":
                        print("Você fugiu da batalha!")
                        return
                    else:
                        print("Opção inválida.")
                        continue
                else:
                    print("2 - Usar item")
                    print("3 - Fugir")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        self.jogador.atacar(inimigo)
                        if inimigo.esta_vivo():
                            inimigo.realizar_turno(self.jogador)
                    elif opcao == "2":
                        self.item.usar(self.jogador)
                    elif opcao == "3":
                        print("Você fugiu da batalha!")
                        return
                    else:
                        print("Opção inválida.")
                        continue

            if not self.jogador.esta_vivo():
                print(f"\n{inimigo.nome} venceu a batalha!")
                return

            print(f"\n{self.jogador.nome} derrotou {inimigo.nome}!")

        print(f"\n{self.jogador.nome} venceu todas as batalhas!")
