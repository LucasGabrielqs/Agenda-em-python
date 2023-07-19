infinito = 1
lista_nome = [] 
lista_numero = []

def adcionar_contato(nome, numero):
    lista_nome.append(nome)
    lista_numero.append(numero)
    return 0
def mostrar_contato():
    for i in range (len(lista_nome)):
        print(lista_nome[i]," ",lista_numero[i])

while infinito != 0:
    print ("|------------Menu------------|")
    print ("1 - Adcionar Contato")
    print("-----------------------------")
    print("2 - Listar todos os contatos")
    print("-----------------------------")
    print("3 - Procurar por nome")
    print("-----------------------------")
    print("4 - Procurar por número") 
    print("-----------------------------")
    print("5 - Alterar contato")
    print("-----------------------------")
    print("6 - Quantidade de contatos")
    print("-----------------------------")
    print("7 - Excluir agenda")
    print("-----------------------------")
    print ("8 - Sair")
    opcao = int(input())
    match opcao:
        case 1:
            nome = input("Digite o nome do contato")
            numero = input("Digite o numero do contato")
            adcionar_contato(nome,numero)
        case 2:
            mostrar_contato()
        case 3:
            print()
        case 4:
            print()
        case 5:
            print()
        case 6:
            print()
        case 7:
            print()
        case 8:
            print()



