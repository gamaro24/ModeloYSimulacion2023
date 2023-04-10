# Librerias necesarias
import matplotlib.pyplot as plt
import numpy

# Condiciones Iniciales - poblacion iniciales, capacidadTerreno y tiempo
liebres = 500
zorros = 10
cap_ter = 5000
semanas = 1000
crecimiento_liebres = 0.08
tasa_mortalidad_zorros = 0
perdida_liebres_caza = 0.002
supervivencia_zorros = 0.0004

# Declaracion poblaciones totales
totalLiebres = list(range(semanas))
totalZorros = list(range(semanas))
for i in range(semanas):
    capActual = cap_ter - liebres
    tasa_lie = (1 / cap_ter) * capActual * crecimiento_liebres * liebres
    sob_zor = tasa_mortalidad_zorros * zorros
    caza = zorros * liebres
    liebres = liebres + (tasa_lie - perdida_liebres_caza * caza)
    zorros = zorros + (supervivencia_zorros * caza - sob_zor)
    totalLiebres[i] = liebres
    totalZorros[i] = zorros
    print("Semana:", i, " Poblacion total liebres: ", liebres, " Poblacion total zorros: ", zorros)

# Asignacion poblaciones y ploteado
xTiempo = numpy.linspace(0, semanas, semanas)
yLiebres = numpy.array(totalLiebres)
yZorros = numpy.array(totalZorros)

plt.plot(xTiempo, yLiebres, label='Liebres', color="blue")
plt.plot(xTiempo, yZorros, label='Zorros', color="orange")
plt.legend(loc="upper right")
plt.title("Diagrama por Tiempo")
plt.xlabel('Tiempo', fontsize=12)
plt.ylabel('Predador-Presa', fontsize=12)
plt.show()
plt.plot(yLiebres, yZorros)
plt.title("Diagrama de fase")
plt.xlabel('Liebres', fontsize=12)
plt.ylabel('Zorros', fontsize=12)
plt.show()
