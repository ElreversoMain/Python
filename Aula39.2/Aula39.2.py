condicao=True
condicao =30
while condicao==30:
    
    deseja=input(f"Deseja comer  coxinha ?: ")
    Transforma=int(deseja)
    print(f"voce comeu {deseja}")
    if Transforma >= 10:
        print(f"eu comi {deseja} estou ficando cheio ")
    if deseja=="30":
        break
    

print("Estou cheio")
 
contador = 0
while contador <=1000:
    contador +=1
    print(contador)
    if contador ==6 :
        print("não vou mostrar o 6.")
        continue

    if contador >= 40 and contador <= 80:
        print("Esta chegando")

    if contador ==100:
        break

print("acabou")