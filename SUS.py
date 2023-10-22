import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Resultados de la encuesta SUS (puntuaciones de los participantes)
sus_scores = [78, 72, 84, 75, 93, 56, 78, 89, 73, 80]

# Calcular el puntaje promedio del SUS
sus_mean = np.mean(sus_scores)

# Etiquetas personalizadas para el eje x
etiquetas = ["Participante 1", "Participante 2", "Participante 3", "Participante 4", "Participante 5", "Participante 6", "Participante 7", "Participante 8", "Participante 9", "Participante 10"]

# Crear un gráfico de barras con etiquetas personalizadas
plt.figure(figsize=(8, 4))
sns.set_style("whitegrid")
barplot = sns.barplot(x=etiquetas, y=sus_scores, palette="Blues_d")
plt.axhline(sus_mean, color='green', linestyle='--', label=f'Media SUS: {sus_mean:.2f}')

# Etiquetas
plt.title("Resultados de la Encuesta de Usabilidad (SUS)")
plt.xlabel("Participantes")
plt.ylabel("Puntuación SUS")
plt.xticks(rotation=45)  # Rotar etiquetas para mayor claridad
plt.legend()

plt.figure(figsize=(6, 2))
plt.axhline(50, color='gray', linestyle='--', label='Inaceptable (0-50)')
plt.axhline(68, color='yellow', linestyle='--', label='Promedio (50-68)')
plt.axhline(100, color='green', linestyle='--', label='Muy Bueno (70-100)')
plt.xlim(0, 100)
plt.ylim(0, 1)  # Ajustar el rango del eje y para una línea horizontal
plt.title("Rangos de Usabilidad")
plt.legend(loc='upper left')
plt.axis('off')  # Ocultar ejes y etiquetas

# Mostrar la gráfica de rangos de usabilidad
plt.show()
# Mostrar el gráfico
plt.tight_layout()
plt.show()

# Crear un DataFrame de pandas para la tabla
data = {"Participante": etiquetas, "Puntuación SUS": sus_scores}
df = pd.DataFrame(data)

# Imprimir la tabla
print("Tabla de Puntuaciones SUS:")
print(df)

