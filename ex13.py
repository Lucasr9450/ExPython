cad = 0
maiorIdade = 0

while True:
    print("\nCadastro ", cad + 1)
    nome = input("Digite o nome do usuário (Digite [encerrar] para parar o programa): ")
    if nome == "encerrar":
        break
    else:
        idade = int(input("Digite a idade do usuário: "))
        if idade >= 18:
            maiorIdade += 1
        cad += 1

print("Número de usuários cadastrados: ", cad, "\nNúmero de maiores de idades cadastrados: ", maiorIdade)