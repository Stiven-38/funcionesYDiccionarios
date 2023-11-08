#IMPRIMIR NÚMEROS EN REVERSA
#Imprime un mensaje que indica que se mostraran numeros en reversa
print("Números en reversa")
#Inicia un bucle for que recorre una secuencia de numeros en reversa Para ello, se utiliza la funcion reversed junto con la funcion range
#range(1, 10, 2) genera una secuencia de números desde 1 hasta 9 con un paso de 2 Esto significa que se generarán los números impares del 1 al 9.
for i in reversed(range(1, 10, 2)):

    print(i)
#Imprime numeros en orden inverso 