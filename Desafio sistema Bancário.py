menu = """

[D] Depositar    [S] Sacar\n
[E] Extrato      [Q] Sair\n

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("A operação falhou! O valor informado é inválido. Tente novamente.")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excede o limite. Por favor, tente pegar um valor menor.")

        elif excedeu_saques:
            print("A operação falhou! Número máximo de saques excedido. Tente novamente amanhã.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("A operação falhou! O valor informado é inválido. Tente novamente.")

    elif opcao == "E":
        print("\n================ EXTRATO ================\n")
        print("Não foram realizadas atividades na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n==========================================\n")

    elif opcao == "Q":
        break

    else:
        print("A operação inválida, por favor selecione novamente a operação desejada.")