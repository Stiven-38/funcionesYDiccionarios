#Accediendo a los elementos de un diccionario
# Creacion de un diccionario llamado 'Diccionario' con dos pares clave-valor
Diccionario = {'nombre': 'Sandra', 'edad': 44}

# Imprime el valor asociado a la clave 'nombre' en el diccionario 'Diccionario'
print(Diccionario['nombre'])

# Imprime el valor asociado a la clave 'nombre' usando el metodo get con un valor predeterminado si la clave no existe
print(Diccionario.get('nombre', 'No existe'))
