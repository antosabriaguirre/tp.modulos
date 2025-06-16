import calculadora_indices as calc

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
edad = int(input("Edad: "))
genero = input("Género (M/F): ").upper()
valor_genero = 5 if genero == 'M' else -161

print("Nivel de actividad:")
print("1. Poco o ningún ejercicio → 1.2")
print("2. Ejercicio ligero (1-3 días) → 1.375")
print("3. Ejercicio moderado (3-5 días) → 1.55")
print("4. Deportista (6-7 días) → 1.72")
print("5. Atleta (2 veces por día) → 1.9")
op = int(input("Seleccione una opción (1-5): "))
valores = [1.2, 1.375, 1.55, 1.72, 1.9]
valor_actividad = valores[op - 1]

tmb_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print(f"Calorías con actividad: {tmb_actividad:.2f}")
