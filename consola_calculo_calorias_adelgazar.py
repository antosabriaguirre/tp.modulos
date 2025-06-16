import calculadora_indices as calc

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
edad = int(input("Edad: "))
genero = input("Género (M/F): ").upper()
valor_genero = 5 if genero == 'M' else -161

mensaje = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
print(mensaje)
