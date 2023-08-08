# Exercicio
nome=input("Digite seu nome ")
idade=input("Digite sua idade ")

if nome or idade != nome and idade:
    print(f"seu nome é {nome} ")
    print("seu nome invertido é ",nome[::-1])
    print(f"primeira letra do seu nome {nome[0]}") #coloquei 0:2
    print(f"Ultima letra do seu nome {nome[-1::]}")
    print("seu nome tem",len(nome),"letras")
    #print(" " in nome," seu nome contém espaço")

if " " in nome:
    print("seu nome contém espaço")

else: 
    print("não contem espaço")


if nome == "" and idade=="":
    print("desculpe digite algo")


# if " " in nome : else : 

#48