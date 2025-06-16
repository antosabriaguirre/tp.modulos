import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calc.calcular_IMC(peso, altura)
print(f"Su IMC es: {imc:.2f}")

