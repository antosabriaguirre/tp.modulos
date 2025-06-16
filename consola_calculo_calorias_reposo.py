import calculadora_indices as calc

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
edad = int(input("Edad: "))
genero = input("Género (M/F): ").upper()
valor_genero = 5 if genero == 'M' else -161

tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print(f"Calorías en reposo (TMB): {tmb:.2f}")
