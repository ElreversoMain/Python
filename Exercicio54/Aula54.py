Carrinho = []
while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar:")
    if opcao == "i":
        print("escolha foi i ")
        valor = input("escolha um valor ")
        Carrinho.append(valor)

    elif opcao=="l":
        for i,valor in enumerate(Carrinho):
            print(i,valor)
        

"""del"""