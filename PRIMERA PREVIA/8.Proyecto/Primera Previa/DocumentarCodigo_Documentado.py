# COMPUTACIÓN BLANDA - Sistemas y Computación

# -----------------------------------------------------------------
# AJUSTES POLINOMIALES
# -----------------------------------------------------------------
# Lección 06
#
# ** Se importan los archivos de trabajo
# ** Se crean las variables
# ** Se generan los modelos
# ** Se grafican las funciones
#
# -----------------------------------------------------------------
# Se importa la librería del Sistema Operativo
# Igualmente, la librería utils y numpy
# -----------------------------------------------------------------
import os
# Directorios: chart y data en el directorio de trabajo
# -----------------------------------------------------------------
from utils import DATA_DIR, CHART_DIR
import numpy as np
# Se eliminan las advertencias por el uso de funciones que
# en el futuro cambiarán
# -----------------------------------------------------------------
np.seterr(all='ignore')
# Se importa la librería scipy y matplotlib
# -----------------------------------------------------------------
import scipy as sp
import matplotlib.pyplot as plt
# Datos de trabajo
# -----------------------------------------------------------------
data = np.genfromtxt(os.path.join("web_traffic.tsv"),delimiter="\t")
# Se establece el tipo de dato
data = np.array(data, dtype=np.float64)
print(data[:10])
print(data.shape)
# Todos los ejemplos tienen tres clases en este archivo
# -----------------------------------------------------------------
colors = ['g', 'k', 'b', 'm', 'r']
linestyles = ['-', '-.', '--', ':', '-']

x = data[:, 0]
y = data[:, 1]
print("Número de entradas incorrectas:", np.sum(np.isnan(y)))
# Se eliminan los datos incorrectos
# -----------------------------------------------------------------
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]
# CON ESTA FUNCIÓN SE DEFINE UN MODELO, EL CUAL CONTIENE
# el comportamiento de un ajuste con base en un grado polinomial
# elegido
# -----------------------------------------------------------------
def plot_models(x, y, models, fname, mx=None, ymax=None, xmin=None):
    ''' dibujar datos de entrada '''
    plt.figure(num=None, figsize=(8, 6))
    plt.clf()
    plt.scatter(x, y, s=10)
    plt.title("Tráfico Web en el último mes")
    plt.xlabel("Tiempo")
    plt.ylabel("Solicitudes/Hora")
    plt.xticks(
        [w * 7 * 24 for w in range(10)],
        ['semana %i' % w for w in range(10)])
    if models:
        if mx is None:
            mx = np.linspace(0, x[-1], 1000)
#--------------------------------------------------------------------------------------------
#AQUI INICIA MI DOCUMENTACIÓN
#  Mediante este for se emparejan las listas models,linestyles,colors
        for model, style, color in zip(models, linestyles, colors):
           #Se generan las líneas de tendencia en cada uno de los gráficos
           plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)
        #Texto que indica el orden de la línea de tendencia dibujada anteriormente
        plt.legend(["d=%i" % m.order for m in models], loc="upper left")
    #Función de matplotlib que determina la escala automáticamente dependiendo del intervalo
    #en el que se encuentran los datos
    plt.autoscale(tight=True)
    #Define el límite mínimo de y en su origen
    plt.ylim(ymin=0)
    #Atributo que define el valor límite de x o y para graficar
    if ymax:
        plt.ylim(ymax=ymax)
    if xmin:
        plt.xlim(xmin=xmin)
    #Dibuja la cuadrícula de referencia en el plano cartesiano
    plt.grid(True, linestyle='-', color='0.75')
    #Guarda la figura generada en el código
    plt.savefig(fname)
# Primera mirada a los datos
# -----------------------------------------------------------------
#Guarda los graficos generados por el código en la carpeta charts
plot_models(x, y, None, os.path.join(CHART_DIR, "1400_01_01.png"))
# Crea y dibuja los modelos de datos
# -----------------------------------------------------------------
#En la función polyfit se crea un listado con los coeficientes del polinomio de orden n
fp1, res1, rank1, sv1, rcond1 = np.polyfit(x, y, 1, full=True)
print("Parámetros del modelo fp1: %s" % fp1)
print("Error del modelo fp1:", res1)
# En la función poly1d sirve como ayuda para definir la función polinomial
f1 = sp.poly1d(fp1)

fp2, res2, rank2, sv2, rcond2 = np.polyfit(x, y, 2, full=True)
print("Parámetros del modelo fp2: %s" % fp2)
print("Error del modelo fp2:", res2)
f2 = sp.poly1d(fp2)

f3 = sp.poly1d(np.polyfit(x, y, 3))
f10 = sp.poly1d(np.polyfit(x, y, 10))
f100 = sp.poly1d(np.polyfit(x, y, 50))

# Se grafican los modelos
# -----------------------------------------------------------------
#Crea los tres archivos de imagen y guarda en ellos los gráficos, y los ubica en
#la carpeta charts
plot_models(x, y, [f1], os.path.join(CHART_DIR, "1400_01_02.png"))
plot_models(x, y, [f1, f2], os.path.join(CHART_DIR, "1400_01_03.png"))
plot_models(x, y, [f1, f2, f3, f10, f100], os.path.join(CHART_DIR,"1400_01_04.png"))

# Ajusta y dibuja un modelo utilizando el conocimiento del punto
# de inflexión
# -----------------------------------------------------------------
inflexion = 3.5 * 7 * 24
xa = x[:int(inflexion)]
ya = y[:int(inflexion)]
xb = x[int(inflexion):]
yb = y[int(inflexion):]

# Se grafican dos líneas rectas
# -----------------------------------------------------------------
fa = sp.poly1d(np.polyfit(xa, ya, 1))
fb = sp.poly1d(np.polyfit(xb, yb, 1))

# Se presenta el modelo basado en el punto de inflexión
# -----------------------------------------------------------------
plot_models(x, y, [fa, fb], os.path.join(CHART_DIR, "1400_01_05.png"))

# Función de error
# -----------------------------------------------------------------
#Se define la diferenica entre los puntos reales y los puntos virtuales
def error(f, x, y):
    return np.sum((f(x) - y) ** 2)
# Se imprimen los errores
# -----------------------------------------------------------------
print("Errores para el conjunto completo de datos:")
#MUESTRA EL ERROR DEFINIDO ANTERIORMENTE PARA CADA ORDEN
for f in [f1, f2, f3, f10, f100]:
    print("Error d=%i: %f" % (f.order, error(f, x, y)))
print("Errores solamente después del punto de inflexión")
for f in [f1, f2, f3, f10, f100]:
    print("Error d=%i: %f" % (f.order, error(f, xb, yb)))
print("Error de inflexión=%f" % (error(fa, xa, ya) + error(fb, xb, yb)))

# Se extrapola de modo que se proyecten respuestas en el futuro
# -----------------------------------------------------------------
plot_models(
    x, y, [f1, f2, f3, f10, f100],
    #Guarda el modelo en la carpeta charts con sus respectivos atributos para la
    #proyecccion a analizar 
    os.path.join(CHART_DIR, "1400_01_06.png"),
    mx=np.linspace(0 * 7 * 24, 6 * 7 * 24, 100),ymax=10000, xmin=0 * 7 * 24)


#HASTA AQUI ES LA TAREA EN SU FASE DE ENTENDIMIENTO Y GENERACIÓN DE COMENTARIOS POR LÍNEA
print("Entrenamiento de datos únicamente despúes del punto de inflexión")
fb1 = fb
fb2 = sp.poly1d(np.polyfit(xb, yb, 2))
fb3 = sp.poly1d(np.polyfit(xb, yb, 3))
fb10 = sp.poly1d(np.polyfit(xb, yb, 10))
fb100 = sp.poly1d(np.polyfit(xb, yb, 100))

print("Errores de los modelos generados")
for f in [fb1, fb2, fb3, fb10, fb100]:
    print("Error d=%i: %f" % (f.order, error(f, xb, yb)))

# Gráficas después del punto de inflexión
# -----------------------------------------------------------------
plot_models(
    x, y, [fb1, fb2, fb3, fb10, fb100],
    os.path.join(CHART_DIR, "1400_01_07.png"),
    mx=np.linspace(0 * 7 * 24, 6 * 7 * 24, 100),
    ymax=10000, xmin=0 * 7 * 24)

# Separa el entrenamiento de los datos de prueba
# -----------------------------------------------------------------
frac = 0.3
split_idx = int(frac * len(xb))
shuffled = sp.random.permutation(list(range(len(xb))))
test = sorted(shuffled[:split_idx])
train = sorted(shuffled[split_idx:])
fbt1 = sp.poly1d(np.polyfit(xb[train], yb[train], 1))
fbt2 = sp.poly1d(np.polyfit(xb[train], yb[train], 2))
print("fbt2(x)= \n%s" % fbt2)
print("fbt2(x)-100,000= \n%s" % (fbt2-100000))
fbt3 = sp.poly1d(np.polyfit(xb[train], yb[train], 3))
fbt10 = sp.poly1d(np.polyfit(xb[train], yb[train], 10))
fbt100 = sp.poly1d(np.polyfit(xb[train], yb[train], 100))

print("Prueba de error para después del punto de inflexión")
for f in [fbt1, fbt2, fbt3, fbt10, fbt100]:
    print("Error d=%i: %f" % (f.order, error(f, xb[test], yb[test])))

plot_models(
    x, y, [fbt1, fbt2, fbt3, fbt10, fbt100],
    os.path.join(CHART_DIR, "1400_01_08.png"),
    mx=np.linspace(0 * 7 * 24, 6 * 7 * 24, 100),
    ymax=10000, xmin=0 * 7 * 24)

from scipy.optimize import fsolve
print(fbt1)
print(fbt1 - 100000)
alcanzado_max = fsolve(fbt1 - 100000, x0=800) / (7 * 24)
print("\n100,000 solicitudes/hora esperados en la semana %f" %alcanzado_max[0])
