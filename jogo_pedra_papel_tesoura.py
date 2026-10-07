import random
sorteio_jogador = ["Pedra","Papel","Tesoura"]
sorteio_computador = ["Pedra","Papel","Tesoura"]

placar_jogador = 0
placar_computador = 0
historico = []

while True:

    opcao = int(input("""===============
Selecione uma jogada para começar:

1 - Pedra. 
2 - Papel.
3 - Tesoura.
4 - Sair
: """)).captalize

    match opcao:

        case 1:
            
            if opcao  == 1:

                sorteio_computador = random.choice(sorteio_computador).capitalize
                if sorteio_computador == "Papel":
                    print(f"""Vencedor dessa rodada foi o COMPUTADOR!

Jogada do Computador = {sorteio_computador}
Jogada Do jogador = {sorteio_jogador} """)

                    placar_computador += 1

                    historico.append(sorteio_jogador,sorteio_computador)

                    print(f"""Historico da partida: {historico}
placar do jogador: {placar_jogador}
Placar do computador: {placar_computador}""")

                    
                else:


                    print(f"""Vencedor dessa rodada foi o JOGADOR!

Jogada do Computador = {sorteio_computador}
Jogada Do jogador = {sorteio_jogador}\n""")
                    
                    placar_jogador += 1

                    historico.append(sorteio_jogador,sorteio_computador)
                    print(f"""Historico da partida: {historico}
placar do jogador: {placar_jogador}
Placar do computador: {placar_computador} \n""")
          

        case 2:

            if opcao == 2:

                sorteio_computador = random.choice(sorteio_computador).capitalize

                if sorteio_computador == "Tesoura":
                    print(f"""Jogada do Computador = {sorteio_computador}
Jogada Do jogador = {sorteio_jogador}\n""")

                    placar_jogador += 1

                    historico.append(sorteio_jogador,sorteio_computador)
                    print(f"""Historico da partida: {historico}
placar do jogador: {placar_jogador}
Placar do computador: {placar_computador}\n""")

                else:

                    #Só cai nessa condição se o jogador 
                    print(f"""Jogada do Computador = {sorteio_computador}
                       Jogada Do jogador = {sorteio_jogador}\n""")
                                           
                    placar_computador += 1
                       
                    historico.append(sorteio_jogador,sorteio_computador)
                    print(f"""Historico da partida: {historico}
                       placar do jogador: {placar_jogador}
                       Placar do computador: {placar_computador}\n""")
                    
            elif sorteio_jogador == sorteio_computador:
                 
                 print(f"Empate entre os jogadores, não a vancedor nessa rodada !")


        case 4:
            print("Você saiu, Obrigado por jogar !")
            break



    

    # if opcao == 1:
    #     print("Bora, vamos jogar de novo !")
    # elif opcao = 2:
    #   print("Obrigado por participar !")
    #      break
    # elif opcao == 3

        

