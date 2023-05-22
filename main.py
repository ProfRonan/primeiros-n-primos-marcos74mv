numTest = int(input("Digite um número: "))

def primoTeste(numero):
    e_primo = True


    for i in range(2, numero):
        if numero % i == 0:
            e_primo = False
            break
    return e_primo

x = 2
while numTest != 0:
    if primoTeste(x) :
        print(x)
        numTest -= 1
    x += 1    