# Define una funcion lambda llamada numero_palabras que toma un argumento "t".
# La funcion lambda realiza las siguientes operaciones:
#  Elimina espacios en blanco iniciales y finales de la cadena "t" utilizando "strip()".
#  Divide la cadena en palabras utilizando "split()".
#  Calcula y devuelve la longitud de la lista resultante que es el número de palabras.
numero_palabras = lambda t: len(t.strip().split())

# Llama a la funcion lambda "numero_palabras" con la cadena "hola esto es una prueba con lambda".
# La funcion cuenta el número de palabras en la cadena y devuelve el resultado.
# Luego, el resultado se imprime en la consola
print(numero_palabras("hola, esto es una prueba con lambda"))
