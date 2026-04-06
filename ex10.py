n = 0
m=""
media = 0
for i in range (1,4):
    print("Nota ",i,"\n")
    n = float(input("Digite a nota: "))
    media += n
media = media/3

if media >= 8:
    m = "A"
elif media >= 5:
    m = "B"
else:
    m = "C"

print("A sua média é ",media,"\nA sua menção é ",m)