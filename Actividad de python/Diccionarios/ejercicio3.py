#Agregar datos al diccionario despues de  creado
# Se asigna el valor 0 a la variable 'calificaciones'.
calificaciones = {}
# update  se utiliza para agregar elementos a un diccionario o actualizar los valores de las claves existentes en este caso se le pasa un diccionario entre llaves que contiene dos nuevos pares clave-valor:
calificaciones.update({"Rosa": 3.7, "German": 4.8})


#Tecnicas de iteracion
 #Esto marca el inicio de la creación del diccionario "calificaciones utilizando llaves.
calificaciones = {
 
#Se agrega el primer par clave-valor al diccionario. La clave es "nombre" y el valor es "Sandra". 
'nombre': 'Sandra',
#Se agrega el segundo par clave-valor al diccionario. La clave es "notafinal" y el valor es 5.0. Esto podría representar la calificación final de alguna evaluacion
'notafinal': 5.0

}

# Creación de un diccionario llamado 'calificaciones' con varios pares clave-valor
calificaciones = {
    'Sandra': 5.0,
    'Adriana': 5.0,
    'Mauricio': 4.5,
    'Jose': 2.5
}
# Itera a través de los elementos (claves y valores) del diccionario 'calificaciones' y los almacena en las variables i y j
for i, j in calificaciones.items():
    # Imprime la clave (i) y el valor (j) del diccionario en cada iteración del bucle  #items() se utiliza para obtener tanto las claves como los valores del diccionario en cada iteracion.
    print(i, j)


#Técnicas de iterar los diccionarios

# Imprime un encabezado que indica que se mostrarán las claves
print("Técnicas por clave")

# Inicia un bucle 'for' que recorre las claves del diccionario 'calificaciones'
for i in calificaciones.keys():
    # keys(). Esto significa que "i" tomara el valor de cada clave en el diccionario en cada iteracion.Imprime cada clave en el diccionario

#En cada iteracion del bucle, se imprime la clave (almacenada en la variable "i"). Esto muestra en la salida todas las claves contenidas en el diccionario "calificaciones"

    print(i)


#Imprime un mensaje que indica que a continuacion se recorreran e imprimiran los valores del diccionario. Esto es un encabezado para dar contexto a la salida
print("Iterar por valor")

#Inicia un bucle for que recorre los valores del diccionario "calificaciones" utilizando el metodo values(). Esto significa que "j" tomará el valor de cada valor en el diccionario en cada iteración.
for j in calificaciones.values():
#en cada iteración del bucle, se imprime el valor (almacenado en la variable "j"). Esto muestra en la salida todos los valores contenidos en el diccionario "calificaciones".
 print(j)
 