import numpy as np
import matplotlib.pyplot as plt

# Intervalo de valores para W
w_values = np.linspace(0, 130, 500)

# Función de distribución acumulativa (CDF) de W
def F_W(w):
    if w < 5:
        return 0
    elif w > 125:
        return 1
    else:
        return (np.sqrt(5 * w) - 5) / 20

# Vectorizando la función para manejar arrays de numpy
F_W_vectorized = np.vectorize(F_W)

# Calculando la CDF para cada valor en w_values
F_W_values = F_W_vectorized(w_values)

# Graficar la CDF de W
plt.plot(w_values, F_W_values, label='$F_W(w)$', color='blue')
plt.title('Función de Distribución Acumulativa (CDF) de W')
plt.xlabel('$w$')
plt.ylabel('$F_W(w)$')
plt.grid(True)
plt.legend()
plt.show()