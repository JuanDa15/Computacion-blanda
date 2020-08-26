import numpy as np
import matplotlib.pyplot as plt

# PROYECTO machine learning

# Enunciado: Una empresa vende el servicio de proporcionar algoritmos de aprendizaje automático a través de HTTP.
# Con el éxito creciente de la empresa, aumenta la demanda de una mejor infraestructura para atender todas las
# solicitudes web entrantes. No queremos asignar demasiados recursos, ya que sería demasiado costoso.
# Por otro lado, perderemos dinero si no hemos reservado suficientes recursospara atender todas las solicitudes entrantes.
# Ahora, la pregunta es, ¿cuándo alcanzaremos el límite de nuestra infraestructura actual, que se estima en
# 100.000 solicitudes por hora?. Nos gustaría saberlo de antemano cuando tenemos que solicitar servidores adicionales
# en la nube para atender todas las solicitudes con éxito sin pagar por las noutilizadas

# Vamos a desarrollar un programa de machine learning (básico)
# El siguiente es un paquete de datos a ser procesdos:
# La primera columna es: Número de hora
# La segunda columna es: Número de tareas ejecutadas

data = np.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10], '\n')
print(data.shape)

x = data[:,0]
y = data[:,1]
print(x, '\n')
print(y, '\n')

print(x.ndim, '\n')
print(y.ndim, '\n')
print(x.shape, '\n')
print(y.shape)

print(np.sum(np.isnan(y)))

print(x.shape, '\n')
print(y.shape, '\n')

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

print(x.shape, '\n')
print(x.shape, '\n')


plt.scatter(x, y, s=10)

plt.title("Tráfico Web en el último mes")
plt.xlabel("Tiempo")
plt.ylabel("Accesos/Hora")
plt.xticks([w*7*24 for w in range(10)],['semana %i' % w for w in range(10)])
plt.autoscale(tight=True)

plt.grid(True, linestyle='-', color='0.75')

plt.show()
#....