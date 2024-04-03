# Definición de una función lambda que suma dos números
suma = lambda x, y: x + y
#Esto solo es una prueba
# Utilizando la función lambda para sumar dos números
resultado = suma(3, 5)
print("El resultado de la suma es:", resultado)

# Ejemplo de cómo usar una función lambda como argumento de otra función
numeros = [1, 2, 3, 4, 5]
# Utilizamos la función lambda para ordenar la lista de números en función de su módulo 2
numeros_ordenados = sorted(numeros, key=lambda x: x % 2)
print("Números ordenados por módulo 2:", numeros_ordenados)
