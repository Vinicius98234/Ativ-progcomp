print ("Calculadora de IMC")

altura = float(input("Informe sua Altura: "))

peso = float(input("Informe seu Peso: "))

imc = (peso) / (altura**2)

print (f"Seu IMC é: {imc}")

if imc > 25 < 29.9:
    print ("Você está no sobrepeso")
elif imc < 24.9 :
    print ("você está com peso normal")
elif imc > 30:
    print ("Você está em obesidade")
