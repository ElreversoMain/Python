Carrinho = []
while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar:")
    if opcao == "i":
        print("escolha foi i ")
        valor = input("escolha um valor ")
        Carrinho.append(valor)

    elif opcao == "a":
        apagar = input("escolha indice para apagar ")
        try:
            indice = int(apagar)
            del Carrinho[indice]
        except ValueError:
            print("porfavor digite numero int")

    elif opcao == "l":
        for i, valor in enumerate(Carrinho):

            print(i, valor)


""" precisei de ajuda pra inserir no append , não consegui fazer delete , lista olhei antigo exercicio"""
"""
Exercicio de Listagem para adicionar,apagar,listar
"""
