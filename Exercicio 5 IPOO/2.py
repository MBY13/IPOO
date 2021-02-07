#Escreva uma função que receba dois números e retorne True
#se o primeiro número for múltiplo do segundo.
#Exemplo de valores esperados: múltiplo(8,4) = True

def multiplo(x,y):
    if (x % y) == int:
        True
    else:
        False

#############################
x = int(input("Digite um numero inteiro:"))
y = int(input("Digite um numero inteiro:"))

if (multiplo(x,y)) == True :
    print (f"Os numeros digitados são multiplo")
else:
    print("Os numeros digitados não são multiplos")