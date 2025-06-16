import calculadora_indices as calc

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
edad = int(input("Edad: "))
genero = input("Género (M/F): ").upper()
valor_genero = 10.8 if genero == 'M' else 0

porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(f"Porcentaje de grasa corporal: {porcentaje_grasa:.2f}%")
