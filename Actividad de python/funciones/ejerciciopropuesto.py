#Ejercicio: Tome el presente ejercicio y pase a la
#funcion la lista con los días de la semana restantes

def lista(arg, result=[]):
    # Agregar el argumento a la lista result
    result.append(arg)
    
    # Imprimir la lista result
    print(result)

# Llamar a la funcion lista con el argumento 'domingo' y una lista vacía
lista('domingo', [])

# Ejercicio: Tomar la lista resultante y pasarla como argumento a la función lista con los días de la semana restantes
def lista(arg, result):
    result.append(arg)

dias_de_la_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']
print("Días de la semana antes de agregar 'domingo':", dias_de_la_semana)

# Llama a la función "lista" con 'domingo' y la lista "dias_de_la_semana" como argumentos
lista('domingo', dias_de_la_semana)

print("Días de la semana después de agregar 'domingo':", dias_de_la_semana)
