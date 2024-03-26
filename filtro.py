import sys

def filtrar_productos(precios, umbral, tipo='mayor'):
    '''Función que filtra los productos según el umbral y el tipo especificados'''
    #Diccionario para almacenar los productos que cumplen el criterio
    productos_filtrados = {}  
    if tipo == 'menor':
        # Filtrar productos cuyo precio es menor que el umbral
        for producto, precio in precios.items():
            if precio < umbral:
                productos_filtrados[producto] = precio
    else:
        # Por defecto, se considera 'mayor' y se filtran los productos cuyo precio es mayor que el umbral
        for producto, precio in precios.items():
            if precio > umbral:
                productos_filtrados[producto] = precio
    return productos_filtrados
# Verificar si el script se ejecuta como programa principal. 

if __name__ == "__main__":
    precios = {'Notebook': 700000, 'Teclado': 25000, 'Mouse': 12000,
            'Monitor': 250000, 'Escritorio': 135000, 'Tarjeta de Video': 1500000}

    if len(sys.argv) == 2:
        # Si se proporciona solo un argumento en la línea de comandos, se considera el umbral
        umbral = int(sys.argv[1])
        # Filtrar productos mayores que el umbral
        productos = filtrar_productos(precios, umbral)
        print("Los productos mayores al umbral son:", ', '.join(productos.keys()))
    elif len(sys.argv) == 3:
        # Si se proporcionan dos argumentos, se considera el umbral y el tipo de filtro (mayor o menor)
        umbral = int(sys.argv[1])
        tipo = sys.argv[2]
        if tipo == 'mayor' or tipo == 'menor':
            # Filtrar productos según el tipo especificado
            productos = filtrar_productos(precios, umbral, tipo)
            if productos:
                # Si hay productos filtrados, imprimir la lista de productos correspondiente al tipo
                if tipo == 'menor':
                    print("Los productos menores al umbral son:", ', '.join(productos.keys()))
                else:
                    print("Los productos mayores al umbral son:", ', '.join(productos.keys()))
            else:
                # Si no hay productos filtrados, imprimir un mensaje indicando que no hay productos que cumplan con el criterio
                print("No hay productos que cumplan con el criterio.")
        else:
            # Si el tipo no es válido, imprimir un mensaje de error
            print("Lo sentimos, no es una operación válida.")
    else:
        # Si no se proporciona el número correcto de argumentos, mostrar un mensaje de uso
        print("Uso: python filtro.py umbral [mayor|menor]")