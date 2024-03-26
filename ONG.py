def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def productora(lista):
    result = 1
    for num in lista:
        result *= num
    return result

def calcular(**kwargs):
    for key, value in kwargs.items():
        # Verifica si la clave comienza con 'fact_'
        if key.startswith('fact_'):
            n = value
            # Calcula el factorial
            print(f"El factorial del número {n} es {factorial(n)}")
        # Verifica si la clave comienza con 'prod_'
        elif key.startswith('prod_'):
            lista = value
            # Calcula la productoria
            print(f"La productora de {lista} es: {productora(lista)}")

if __name__ == "__main__":
    # Prueba de funcionamiento del script, de acuerdo a las instrucciones del desafío
    calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6)