saldo = 1000
while True:
    print("\n--- MENU BANCO TESTE ---")
    print("1 - Ver saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Outros")
    print("5 - Sair")
    chose = int(input("Escolha uma das opções acima: "))
    
    if chose == 1:
        print(f"Seu saldo atual é de R$ {saldo}.")
        input("\nPressione ENTER para voltar para o menu...")
    elif chose == 2:
        print(f"Seu saldo atual é de R${saldo}")
        saque = float(input("Quanto deseja sacar: "))
        
        if saque > saldo:
            print("ERRO: Saldo insuficiente.")
            input("\nPressione ENTER para voltar para o menu...")
        elif saque <= 0:
            print("ERRO: Número inválido.")
            input("\nPressione ENTER para voltar para o menu...")
        else:
            saldo = saldo - saque 
            print(f"Saque realizado com sucesso seu novo saldo é de R${saldo}.")
            input("\nPressione ENTER para voltar para o menu...")
    elif chose == 3:
        print(f"Seu saldo atual é de R${saldo}.")
        deposito = float(input("Quanto deseja depositar: "))
        if deposito < 0:
            print("ERRO: Valor de depósito inválido.")
            input("\nPressione ENTER para voltar para o menu...")
        else:
            saldo = saldo + deposito
            print(f"Depósito realizado com sucesso seu saldo atual é de R${saldo}.")
            input("\nPressione ENTER para voltar para o menu...")
    elif chose == 4:
        print("1 - Falar com um de nosso atendentes.")
        print("2 - Comunicar erro de sistema.")
        print("3 - Avaliar serviço")
        chose2 = int (input("Escolha uma das opções acima. "))
        if chose2 == 1:
            print("Direcionando a um de nossos atendentes, por favor aguarde...")
            input("\nPressione ENTER para voltar para o menu...")
        elif chose2 == 2:
            erro = input("Por favor informe o erro de sistema: ")
            input("\nPressione ENTER para voltar para o menu...")
        elif chose2 == 3:
            avaliacao = input("Por favor de uma nota de 1 a 5 para o nosso sistema :).")
            input("\nPressione ENTER para voltar para o menu...")
        else:
            print("Por favor escolha uma das opções acima")
            input("\nPressione ENTER para voltar para o menu...")
    elif chose == 5:
        print("Saindo do sistema...")
        break
    else:
        print("Por favor selecione um número válido.")
        input("\nPressione ENTER para voltar para o menu...")
