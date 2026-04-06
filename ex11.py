senha = "utf8mb4"
tenta = 0
for i in range (1,4):
    print("Tentativa ",i)
    tenta = input("Digite a senha: ")
    if tenta == senha:
        print("Acesso permitido :)")
        break;
    else:
        print("Senha errada...\n")
if tenta != senha:
    print("Acesso bloqueado :(")