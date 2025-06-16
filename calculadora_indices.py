def calcular_IMC(peso, altura):
    """
    calcula el Índice de Masa Corporal (IMC).
    
    formula:
        IMC = peso / altura²

    parametros:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.

    retorna:
        float: Valor del IMC.
    """
    return peso / (altura ** 2)


def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    """
    calcula el porcentaje de grasa corporal estimado.

    Fórmula:
        %GC = 1.2 * IMC + 0.23 * edad - 5.4 - valor_genero

    parámetros:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.
        edad (int): Edad en años.
        valor_genero (float): 10.8 si es masculino, 0 si es femenino.

    retorna:
        float: Porcentaje de grasa corporal.
    """
    imc = calcular_IMC(peso, altura)
    return 1.2 * imc + 0.23 * edad - 5.4 - valor_genero


def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    """
    calcula la Tasa Metabólica Basal (calorías que el cuerpo quema en reposo)

    fórmula:
        TMB = 10 * peso + 6.25 * altura(cm) - 5 * edad + valor_genero

    parámetros:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.
        edad (int): Edad en años.
        valor_genero (int): 5 si es masculino, -161 si es femenino.

    Retorna:
        float: TMB (calorías quemadas en reposo).
    """
    return (10 * peso) + (6.25 * altura * 100) - (5 * edad) + valor_genero


def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    """
    calcula el gasto calórico según nivel de actividad física.

    fórmula:
        TMB_actividad = TMB * valor_actividad

    parámetros:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.
        edad (int): Edad en años.
        valor_genero (int): 5 si es masculino, -161 si es femenino.
        valor_actividad (float): Factor según actividad (1.2 a 1.9).

    retorna:
        float: Calorías estimadas con actividad física.
    """
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return tmb * valor_actividad


def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    """
    calcula el rango recomendado de calorías diarias para adelgazar.

    fórmula:
        Consumo recomendado = 80% a 85% del TMB

    parámetros:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.
        edad (int): Edad en años.
        valor_genero (int): 5 si es masculino, -161 si es femenino.

    retorna:
        str: Texto con el rango recomendado de calorías para adelgazar.
    """
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = tmb * 0.80
    rango_superior = tmb * 0.85
    return f"Para adelgazar es recomendado que consumas entre: {rango_inferior:.2f} y {rango_superior:.2f} calorías al día."

