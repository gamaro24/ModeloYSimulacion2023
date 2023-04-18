# Librerias necesarias
import matplotlib.pyplot as plt
import numpy

# Condiciones Iniciales - poblacion iniciales, capacidadTerreno y tiempo
liebres = 2500
zorros = 2
cap_ter = 1400
semanas = 1000
crecimiento_liebres = 0.08
tasa_mortalidad_zorros = 0.2
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

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Semanas')
ax1.set_ylabel('Liebres', color=color)
ax1.plot(xTiempo, yLiebres, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Zorros', color=color)  # we already handled the x-label with ax1
ax2.plot(xTiempo, yZorros, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()


plt.plot(yLiebres, yZorros)
plt.title("Diagrama de fase")
plt.xlabel('Liebres', fontsize=12)
plt.ylabel('Zorros', fontsize=12)
plt.show()
