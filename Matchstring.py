Comando = input("Digite o seu comando: ")

match Comando:
    case "oi" | "OI" | "Oi":
        print("o seu comando foi oi")
    case "tchau":
        print("o seu comando foi tchau")
    case "Como vai":
        print("o seu comando foi como vai")
    case _:
        print("Comando invalido")              