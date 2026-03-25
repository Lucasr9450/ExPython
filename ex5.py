Nome = input("Digite o nome do jogador")
Sal = int(input("Digite o salário do jogador"))
if Sal<=1000:
    print(Nome, Sal*1.10)
elif Sal>1000.01 and Sal<=5000:
    print(Nome, Sal*1.10)
else:
    print(Nome, Sal*1.05)