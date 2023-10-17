import random

nove_digitos=""
for i in range(11):
    nove_digitos +=str(random.randint(0,11))

print(nove_digitos)

colocar =input("Digite seu cpf:" )
numero_1 = int(colocar[0])*10
numero_2 = int(colocar[1])*9
numero_3 = int(colocar[2])*8
numero_4 = int(colocar[3])*7
numero_5 = int(colocar[4])*6
numero_6 = int(colocar[5])*5
numero_7 = int(colocar[6])*4
numero_8 = int(colocar[7])*3
numero_9 = int(colocar[8])*2
somar = numero_1+numero_2+numero_3+numero_4 + \
    numero_5+numero_6+numero_7+numero_8+numero_9
multipicar = somar*10
divisao = multipicar % 11
resultado=divisao

numero_01 = int(colocar[0])*11
numero_02 = int(colocar[1])*10
numero_03 = int(colocar[2])*9
numero_04 = int(colocar[3])*8
numero_05 = int(colocar[4])*7
numero_06 = int(colocar[5])*6
numero_07 = int(colocar[6])*5
numero_08 = int(colocar[7])*4
numero_09 = int(colocar[8])*3
numero_10 = int(colocar[9])*2
somarr = numero_01+numero_02+numero_03+numero_04+numero_05 + \
    numero_06+numero_07+numero_08+numero_09+numero_10
multiplicarr = somarr*10
dividir = multiplicarr % 11
resultado2=dividir

teste=int(colocar[9])
teste2=int(colocar[10])



if  teste  == resultado  :
    print("CPF valido")
else:
    print("invalido")

if teste2==resultado2:
    print("CPF valido")
else:
    print("Invalido")


