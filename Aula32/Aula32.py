#Exercicio

Digite_Numero_Inteiro=input("Digite um numero inteiro: ")
Transforma_Em_Numero=int(Digite_Numero_Inteiro)

if Transforma_Em_Numero % 2 ==0 :
    print("Numero e Par")
else:
    print("Numero e Impar")

    Pergunte_Horario=input("Digite Horário Desejado: ")
Transforma=int(Pergunte_Horario)

# esse eu consegui fazer mas esqueci sinal % coloquei // funcionou mas não era certo


Pergunte_Horario=input("Digite Horário Desejado: ")
Transforma=int(Pergunte_Horario)
if Transforma >=0 and Transforma <=11:
    print("Bom dia")
elif Transforma >= 12 and Transforma <=17 :
    print("Boa Tarde")
elif Transforma >= 18 and Transforma <=23 :
    print("Boa noite")
"""
if Transforma <= 11 :
    print("Bom dia")
elif Transforma > 12 :
    print("Boa Tarde")
elif Transforma < 18 :
    print("Boa noite")
 forma que eu fiz
"""
# errei na parte dos sinais e no and



nome=input("Digite seu nome ")
Tamanho_nome=int(len(nome))

if Tamanho_nome <= 4:
    print("Nome Curto")
elif Tamanho_nome  >= 5 and Tamanho_nome <= 6:
    print("Seu nome e Normal")
else :
    print("Seu nome e Gigante") 

"""
precisar colocar if e elif se fizer separado if bloco não dependera

errei na forma colocar sinais e no and 
if TransformaSTR <4:
elif TransformaSTR >5 == 6:
elif TransformaSTR < 6 """