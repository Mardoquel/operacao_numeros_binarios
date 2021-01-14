import os
import SomaBinario
import SubtracaoBinario
import MultiplicacaoBinario
import DivisaoBinario

def menu_principal():
    
    while(True):
        print("===== MENU INTERATIVO =====")
        print("SELECIONE UMA DAS OPÇÕES ABAIXO:")
        print("[1]Soma")
        print("[2]Subtração")
        print("[3]Multiplicação")
        print("[4]Divisão")
        print("Se quiser encerrar o programa digite 'sair'")
        opcao = input("OPÇÃO: ")
        os.system('cls')

        if opcao.lower() == 'sair':
            print("\nFim do Programa!")
            exit(0)



        elif opcao == '1':
            SomaBinario.soma()

        elif opcao == '2':
            SubtracaoBinario.subtracao()

        elif opcao == '3':
            MultiplicacaoBinario.multiplicacao()

        elif opcao == '4':
            DivisaoBinario.divisão()

        else:
            print("Opção inválida, tente novamente\n")
            os.system('pause')
            os.system('cls')
            continue