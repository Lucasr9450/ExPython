idade = int(input("Digite a sua idade: "))
def maioridade():
    if(idade >= 18):
        return "Maior de idade"
    else:
        return "Menor de idade"
idade2 = maioridade()
print(idade2)