import numpy as np

#Crea un arreglo numerico con valores del 0 a n
array = np.arange(6)
print('arreglo array= ',array,'\n')
print('Tipo de array= ',array.dtype,'\n')
#Se muestra la dimension del array en este caso 1 por ser un vector
print('Dimension del array = ',array.ndim,'\n')
print('Numero de elementos = ' , array.shape,'\n')


#Crear una matriz
Matriz = np.array([np.arange(2),np.arange(2)])
print(Matriz)

a = np.array([[1,2], [3,4]])
print('a =\n', a, '\n')
#Seleccion de elementos individuales de una matriz
print('a[0,0] =', a[0,0], '\n')
print('a[0,1] =', a[0,1], '\n')
print('a[1,0] =', a[1,0], '\n')
print('a[1,1] =', a[1,1])


a = np.arange(9)
print('a =', a, '\n')
print('a[0:9] = ', a[0:9], '\n')
#Se puede imprimir en un rango entre la longitud del arreglo
print('a[3,7] =', a[3:7])
#Agregando un numero despues del rango de numeros que se quieren se puede crear una secuencia para imprimir los numeros ya sea de 2 en 2...
print('a[0:9:1] =', a[0:9:1], '\n')
print('a[:9:1] =', a[:9:1], '\n')
print('a[0:9:2] =', a[0:9:2], '\n')
print('a[0:9:3] =', a[0:9:3])
#Con el incremento negativo se muestra en orden inverso
print('a[9:0:-1] =', a[9:0:-1], '\n')
print('a[::-1] =', a[::-1])

#Se estructura un arreglo de 24 posiciones en una matriz  de 2 bloques 3 filas y 4 columnas con reshape
b = np.arange(24).reshape(2,3,4)
print('b =\n', b)
#Acceso  a la matriz re estructurada
print('b[1,2,3] =', b[1,2,3], '\n')
print('b[0,2,2] =', b[0,2,2], '\n')
print('b[0,1,1] =', b[0,1,1])
#Se puede seleccionar la misma posicion de dos bloques distintos poniendo solo 2 puntos en lugar de un identificador del bloqie
print('b[0,0,0] =', b[0,0,0], '\n')
print('b[1,0,0] =', b[1,0,0], '\n')
print('b[:,0,0] =', b[:,0,0])
#Para imprimir solo el bloque se omiten los demas numeros o simplemente poniendo 2 puntos en la posicion de los demas numeros
print('b[0] =\n', b[0])
print('b[0,:,:] =\n', b[0,:,:])
print('b[0, ...] =\n', b[0, ...])

print('b[0,1] =', b[0,1])
#Se pueden tomar valores de una matriz y llevarlos a una variable
z = b[0,1]
print('z =', z, '\n')
print('z[::2] =', z[::2])
print('b[0,1,::2] =', b[0,1,::2])

print(b, '\n')
print('b[:,:,1] =\n', b[:,:,1], '\n')
print('b[...,1] =\n', b[...,1])

print(b, '\n')
print('b[:,1] =', b[:,1])

print(b, '\n')
print('b[0,:,1] =', b[0,:,1])
#Para seleccionar la ultima columna del primer bloque basta con poner un -1 en la posicion de la columna
print('b[0,:,-1] =', b[0,:,-1])

print('b[0, ::-1, -1] =', b[0, ::-1, -1])
print('b[0, ::-1, -1] =', b[0, ::-1, -1])
print('b[0, ::2, -1] =', b[0, ::2, -1])

print(b, '\n-----------------------\n')
print(b[::-1])
#Con el metodo ravel se puede generar un vector a travez de la matriz
print('Matriz b =\n', b, '\n--------------------------\n')
print('Vector b = \n', b.ravel())
#Similar al anterior solo que este crea un nuevo espacio de memoria
print('Vector b con flatten =\n', b.flatten())
#Se re estructura la matriz
b.shape = (6,4)
print('b(6x4) =\n', b)

# Matriz original
print('b =\n', b, '\n------------------------\n')
# Matri transpuesta
print('Transpuesta de b =\n', b.transpose(), '\n------------------------\n')

#Similar a reshape la unica diferencia es que este modifica la estructura del array y reshape no
# Matriz original
print('b =\n', b, '\n------------------------\n')
# Matri transpuesta
print('Transpuesta de b =\n', b.transpose(), '\n------------------------\n')

# APILAMIENTO
# -----------
# Apilado
# Las matrices se pueden apilar horizontalmente, en profundidad o
# verticalmente. Podemos utilizar, para ese propósito,
# las funciones vstack, dstack, hstack, column_stack, row_stack y concatenate.
# Para empezar, vamos a crear dos arrays
# Matriz a
a = np.arange(9).reshape(3,3)
print('a =\n', a, '\n')
# Matriz b, creada a partir de la matriz a
b = a*2
print('b =\n', b)
# Utilizaremos estas dos matrices para mostrar los mecanismos
# de apilamiento disponibles

# APILAMIENTO HORIZONTAL
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento horizontal
print('Apilamiento horizontal =\n', np.hstack((a,b)) )


# APILAMIENTO HORIZONTAL - Variante
# Utilización de la función: concatenate()
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento horizontal
print( 'Apilamiento horizontal con concatenate = \n',
np.concatenate((a,b), axis=1) )
# Si axis=1, el apilamiento es horizontal

# APILAMIENTO VERTICAL
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical
print( 'Apilamiento vertical =\n', np.vstack((a,b)) )

# APILAMIENTO VERTICAL - Variante

# Utilización de la función: concatenate()
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical
print( 'Apilamiento vertical con concatenate =\n',
np.concatenate((a,b), axis=0) )
# Si axis=0, el apilamiento es vertical

# APILAMIENTO EN PROFUNDIDAD

# En el apilamiento en profundidad, se crean bloques utilizando
# parejas de datos tomados de las dos matrices
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento en profundidad
print( 'Apilamiento en profundidad =\n', np.dstack((a,b)) )

# APILAMIENTO POR COLUMNAS

# El apilamiento por columnas es similar a hstack()
# Se apilan las columnas, de izquierda a derecha, y tomándolas
# de los bloques definidos en la matriz
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical
print( 'Apilamiento por columnas =\n',np.column_stack((a,b)) )

# APILAMIENTO POR FILAS

# El apilamiento por fila es similar a vstack()
# Se apilan las filas, de arriba hacia abajo, y tomándolas
# de los bloques definidos en la matriz
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical
print( 'Apilamiento por filas =\n',np.row_stack((a,b)) )
# DIVISIÓN DE ARRAYS

# Las matrices se pueden dividir vertical, horizontalmente o en profundidad.
# Las funciones involucradas son hsplit, vsplit, dsplit y split.
# Podemos hacer divisiones de las matrices utilizando su estructura inicial
# o hacerlo indicando la posición después de la cual debe ocurrir la división
# DIVISIÓN HORIZONTAL
print(a, '\n')
# El código resultante divide una matriz a lo largo de su eje horizontal
# en tres piezas del mismo tamaño y forma:}
print('Array con división horizontal =\n', np.hsplit(a, 3), '\n')
# El mismo efecto se consigue con split() y utilizando una bandera a 1
print('Array con división horizontal, uso de split() =\n',np.split(a, 3, axis=1))

# DIVISIÓN VERTICAL
print(a, '\n')
# La función vsplit divide el array a lo largo del eje vertical:
print('División Vertical = \n', np.vsplit(a, 3), '\n')
# El mismo efecto se consigue con split() y utilizando una bandera a 0
print('Array con división vertical, uso de split() =\n',
np.split(a, 3, axis=0))

# DIVISIÓN EN PROFUNDIDAD

# La función dsplit, como era de esperarse, realiza división
# en profundidad dentro del array
# Para ilustrar con un ejemplo, utilizaremos una matriz de rango tres
c = np.arange(27).reshape(3, 3, 3)
print(c, '\n')
# Se realiza la división
print('División en profundidad =\n', np.dsplit(c,3), '\n')

# El atributo ndim calcula el número de dimensiones

print(b, '\n')
print('ndim: ', b.ndim)

# El atributo size calcula el número de elementos

print(b, '\n')
print('size: ', b.size)

# El atributo itemsize obtiene el número de bytes por cada

# elemento en el array
print('itemsize: ', b.itemsize)

# El atributo itemsize obtiene el número de bytes por cada

# elemento en el array
print('itemsize: ', b.itemsize)

# El atributo T tiene el mismo efecto que la transpuesta de la matriz

b.resize(6,4)
print(b, '\n')
print('Transpuesta: ', b.T)

# Los números complejos en numpy se representan con j

b = np.array([1.j + 1, 2.j + 3])
print('Complejo: \n', b)

# El atributo real nos da la parte real del array,
# o el array en sí mismo si solo contiene números reales
print('real: ', b.real, '\n')
# El atributo imag contiene la parte imaginaria del array
print('imaginario: ', b.imag)

# Si el array contiene números complejos, entonces el tipo de datos

# se convierte automáticamente a complejo
print(b.dtype)

# El atributo flat devuelve un objeto numpy.flatiter.
# Esta es la única forma de adquirir un flatiter:
# no tenemos acceso a un constructor de flatiter.
# El apartamento El iterador nos permite recorrer una matriz
# como si fuera una matriz plana, como se muestra a continuación:
# En el siguiente ejemplo se clarifica este concepto
b = np.arange(4).reshape(2,2)
print(b, '\n')
f = b.flat
print(f, '\n')
# Ciclo que itera a lo largo de f
for item in f: print (item)
# Selección de un elemento
print('\n')
print('Elemento 2: ', b.flat[2])
# Operaciones directas con flat
b.flat = 7
print(b, '\n')
b.flat[[1,3]] = 1
print(b, '\n')