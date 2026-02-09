def analizar_numeros(lista_numeros):

    """
    Analiza una lista de numero enteros y retorna estadisticas basicas

    Args:
        lista_numeros (list): Lista de números enteros a analizar
    
    Returns:
        tuple: (pares, impares, promedio, numero_mayor, numero_menor)
    """
    if len(lista_numeros) == 0:
        return {"error": "La lista no puede estar vacía"}

    contador_pares = 0
    contador_impares = 0
    promedio = 0
    numero_mayor = lista_numeros[0]
    numero_menor = lista_numeros[0]
    for i in (lista_numeros):
        if i % 2 == 0: contador_pares += 1
        else: contador_impares += 1
        if i > numero_mayor: numero_mayor = i
        if i < numero_menor: numero_menor = i
        promedio += i
    
    promedio = promedio / len(lista_numeros)
        
    return {
        "pares": contador_pares,
        "impares": contador_impares,
        "promedio": promedio,
        "numero_mayor": numero_mayor,
        "numero_menor": numero_menor,
    }

print(analizar_numeros([7]))