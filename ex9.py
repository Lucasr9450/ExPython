peso= float(input("Qual é seu peso?\n"))
altura=float(input("Qual a sua altura?\n"))
imc= peso/(altura*altura)
if imc<18.5:
    print("Abaixo do peso")
elif imc>=18.5 and imc<24.9:
    print("Peso normal")
elif imc >=24.9 and imc <29.9:
    print("Acima do peso")
elif imc >=29.9 and imc<34.9:
    print("Obesidade grau 1")
elif imc>=34.9 and imc<39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")