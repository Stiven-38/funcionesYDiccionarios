# Definición de dos listas, una con nombres y la otra con edades
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']

# Inicia un bucle 'for' que combina elementos de ambas listas y muestra un mensaje formateado zip para combinar elementos de las listas "nombres" y "edades. Esto significa que en cada iteración, "n" tomara un nombre de la lista "nombres" y "e" tomará la edad correspondiente de la lista "edades".

for n, e in zip(nombres, edades):
    # Imprime un mensaje formateado con el nombre y la edad
    #se utiliza para imprimir un mensaje formateado que incluye variables o valores en posiciones específicas dentro del texto
    print('Tú nombre es {0} y tu edad {1}.'.format(n, e))



#esta línea utiliza una expresión de diccionario para crear un nuevo diccionario llamado "dicaleatorio". La expresión de diccionario incluye un bucle for que recorre una secuencia de números (2, 4 y 6) y crea pares clave-valor en el diccionario.
dicaleatorio={x: x**2 for x in (2, 4, 6)}
#Para cada valor "x" en la secuencia, se calcula "x**2" y se utiliza como valor del diccionario, mientras que "x" se utiliza como clave.
#En este caso, se generarán los siguientes pares clave-valor: {2: 4, 4: 16, 6: 36}

#Esta línea imprime el diccionario "dicaleatorio" en la salida. En este ejemplo, se mostrara el diccionario creado en el paso anterior
print(dicaleatorio)