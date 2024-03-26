#Calcular el promedio de una lista de velocidades en Python
def promedio_velocidades(velocidades):
    return sum(velocidades) / len(velocidades)

def correas_sobre_promedio(velocidades):
    promedio = promedio_velocidades(velocidades)
    return [i for i, v in enumerate(velocidades) if v > promedio]

if __name__ == "__main__":
    # Lista de velocidades
    velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
                14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

    # Calcula el promedio de las velocidades
    promedio = promedio_velocidades(velocidad)

    # Encuentra las correas con velocidades sobre el promedio
    correas_sobre_promedio = correas_sobre_promedio(velocidad)

    # Imprime los resultados extrapolaados
    print(f"Promedio de velocidades: {promedio}")
    print(f"Correas con velocidades sobre el promedio: {correas_sobre_promedio}")