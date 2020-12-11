# Se importa la librería numpy
import numpy as np
# Se crea un vector (array) con seis elementos
a = np.array([0,1,2,3,4,5])
# Se imprime el array ... a
print(a, '\n')
# Número de dimensiones del array
print(a.ndim, '\n')
# Número de elementos del array
print(a.shape)
print("--------------------------------------------------")
# Se cambia la estructura del array
b = a.reshape((3,2))
print(b, '\n')
# Se verifican los cambios
print(b.ndim, '\n')
print(b.shape)
# Se modifica el primer elemento de la segunda fila
b[1][0] = 77
# Se verifica el cambio
print("b =",b)
# Debido a que el array b se construyo con base en el array a, el cambio afecta también al array a
print("a =",a)
# Se realiza una copia del array
c = a.reshape((3,2)).copy()
print("c =",c, '\n')
# Se cambia el primer valor de c
c[0][0] = -99
# El array a no se modifica
print(a, '\n')
# El array c queda modificado
print(c)
# Las operaciones se propagan a lo largo del array
d = np.array([1,2,3,4,5])
# Se multiplican los elementos por 2
print(d*2, '\n')
# Se elevan al cuadrado los elementos del array
print(d**2)