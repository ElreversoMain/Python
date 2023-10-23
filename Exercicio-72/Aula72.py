
def Texte():
    x=16
    if x % 2 == 0:
        print(f"numero {x} é par")
    else:
        print(f"numero {x} e impar")
Texte()

def soma (*args):
    total=1
    for numero in args:
        total *=numero
    return total
multiplicacao=1*2*3*4*5*10
print(multiplicacao)