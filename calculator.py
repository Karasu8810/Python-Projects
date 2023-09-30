import math

primeiro = ""
segundo = ""

def CheckPI():
    global primeiro, segundo
    if primeiro.isdigit() == False :
        primeiro.lower()
        if primeiro == "pi" :
            primeiro = str(math.pi)
    if segundo.isdigit() == False:
        segundo.lower()
        if segundo == "pi" :
            segundo = str(math.pi)

def continuar():
    cont = input("Deseja continuar? (y/n) > ")
    if cont == "y" :
        print("\n\n")
        menu()
    else:
        None

def Soma():
    global primeiro, segundo
    print("-- Soma --\n\n Digite os 2 numeros em sequencia para poder reaizar a soma")
    primeiro = input("Numero 1 > ")
    segundo = input("Numero 2 > ")
    CheckPI()
    if primeiro.replace('.','1').isdigit() == True and segundo.replace('.','1').isdigit() == True:
        soma = float(primeiro) + float(segundo)
        print("\nSoma:",soma,"\n\n")
        continuar()
    else:
        print("\n\n\nRetorne um valor valido!!!\n\n")
        Soma()

def menu():
    print("Seja Bem-Vindo \n O que deseja fazer?\n\n Digite 1 se - Somar 2 numeros\n Digite 2 se - Subtrair 2 numeros\n Digite 3 se - Multiplicar 2 numeros\n Digite 4 se - Dividir 2 numeros\n Digite 5 se - Potenciar 1 numero pelo 2\n Digite 6 se - Tirar a raiz de 1 numero")
    print("\n-- Regras --\n 1- Utilize apenas valores numericos validos\n 2- Se for utilizar o pi, escreva apenas pi\n 3- Ferramente feita apenas para teste de repositorio, nao critique sua simplicidade\n")
    acao = input("> ")
    if acao.isdigit() == True :
        acao = int(acao)
    match acao:
        case 1:
            Soma()
        case _ :
            print("\n\n\nNao temos essa opcao!!!\n\n")
            menu()
        

menu()