#Definir una funcion
# Definicion de una funcion llamada saludar
def saludar():
    print("saludo")

#El cuerpo de esta funcion esta vacío no realiza ninguna accion
def retornarnumero():

#return 1 Esto significa que la funcion devuelve el valor entero 1 al punto donde se llamo
    return 1 

# saludar veras la palabra saludo impresa en la pantalla
saludar()

#Esto llama a la funcion retornarnumero que has definido previamente La funcion retornarnumero devuelve el valor 1 cuando se llama Sin embargo en este caso no esta capturando el valor devuelto ni haciendo nada con el La funcion se llama pero el resultado se descarta
retornarnumero()

#Esto inicia una comprobacion condicional Primero llama nuevamente a la funcion retornarnumero() y compara su valor de retorno con 1. Si la funcion devuelve 1, la condicion es verdadera y el bloque de codigo indentado que sigue se ejecutara Si la funcion no devuelve 1 la condicion es falsa y el bloque de codigo indentado no se ejecutara
if retornarnumero()==1:


    print("devolvio un uno")

else:

    print("No devolvio un uno")