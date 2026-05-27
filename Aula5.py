#print ("1 - cadastrar |  2 - listar | 3 - sair") 

#opcao = int(input("Escolha um opção : "))

# match opcao: 
#    case 1:
#        print("Voce escolheu CADASTRAR")
#    case 2:
#        print("Voce escolheu LISTAR")
#    case 3:
#        print("Voce escolheu SAIR") 
#    case _:
#        print("Opção invalida") 

# mes = int(input("Informe o Número do Mês de: "))   

# match mes:
#     case 1:
#         print("Mês de: JANEIRO")
#     case 2:
#         print("Mês de: FEVEREIRO")
#     case 3:
#         print("Mês de: MARÇO")
#     case 4:
#         print("Mês de: ABRIL")
#     case 5:
#         print("Mês de: MAIO")
#     case 6:
#         print("Mês de: JUNHO")
#     case 7:
#         print("Mês de: JULHO")
#     case 8:
#         print("Mês de: AGOSTO")    
#     case 9:
#         print("Mês de: SETEMBRO")
#     case 10:
#         print("Mês de: OUTUBRO")
#     case 11:
#         print("Mês de: NOVEMBRO")
#     case 12:
#         print("Mês de: DEZEMBRO")         
#     case _ :
#         print("Opção invalida!")        

Plampada = float(input("Digite a potencia da lampada (em Watts): "))
LComodo = float(input("Digite a largura do comodo: "))
Ccomodo = float(input("Digite o comprimento do comodo: "))
area = LComodo * Ccomodo
Tcomodo = int(input("1 - Sala | 2 - Cozinha | 3 - Quarto :  "))

match Tcomodo:
    case 1:
        Wmetro = 100
        Cfinal = (area * Wmetro) / Plampada
        print(F"A quantidade necessaria de lampadas é {Cfinal}")
    case 2:
        Wmetro = 100
        Cfinal = (area * Wmetro) / Plampada
        print(F"A quantidade necessaria de lampadas é {Cfinal}")
    case 3:
        Wmetro = 100
        Cfinal = (area * Wmetro) / Plampada
        print(F"A quantidade necessaria de lampadas é {Cfinal}")