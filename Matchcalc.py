
numero1 = float(input("Informe o Número 1 : "))   
numero2 = float(input("Informe o Número 2 : "))  
operacao = input("Informe a Operacao:  ")

match operacao: 
    case "+": 
        print(numero1 + numero2)
    case "-": 
        print(numero1 - numero2) 
    case "*": 
        print(numero1 * numero2)
    case "/": 
        print(numero1 / numero2)   
    case _: 
        print("Operação Invalida")          
        