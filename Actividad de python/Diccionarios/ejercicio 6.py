# BORRAR UN ELEMENTO DEL DICCIONARIO
# Creación de un diccionario llamado calificaciones con varios pares clave-valor
calificaciones = {
    'camilo': 5.0,
    'Andrea': 4.5,
    'Felipe': 3.0,
    'Cristian': 2.5
}


#Esta línea de código inicia una estructura condicional utilizando la declaración if Verifica si la clave rosa en minusculas esta presente en el diccionario calificaciones El uso de in se utiliza para comprobar si una clave existe en el diccionario.
if 'rosa' in calificaciones:

#Si la clave 'rosa' está presente en el diccionario, esta línea utiliza la declaración del para eliminar esa clave y su valor del diccionario. Nota que en esta línea se utiliza 'Rosa' con mayúscula inicial, lo cual puede causar que la condición en la línea anterior nunca sea verdadera debido a la diferencia entre mayúsculas y minúsculas

    del calificaciones['Rosa']
    


    #Si la clave 'rosa' fue eliminada en la línea anterior, esta línea imprime un mensaje que indica que 'Rosa' fue eliminado del diccionario.
    print("'Rosa' eliminado del diccionario")

# Itera a través del diccionario 'calificaciones' después de eliminar la clave 'Rosa' e imprime las claves y sus valores restantes.
for i, j in calificaciones.items():
    print(i, j)
