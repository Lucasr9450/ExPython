vz = 0
media = 0
nota = 0
maiorNota=0
menorNota = 0

while True:
    print("\nNota ",vz + 1)
    nota = float(input("Digite a nota (Digite [-1] para parar o programa): "))
    if nota != -1:
        if vz == 0:
            maiorNota = nota
            menorNota = nota
            
        media += nota
        
        if nota > maiorNota:
            maiorNota = nota
        
        if nota < menorNota:
            menorNota = nota
        
        vz += 1
    else:
        media = media / vz
        break

print ("A média do aluno foi: ", media, "\nA maior nota foi: ", maiorNota, "\nA menor nota foi: ",menorNota)