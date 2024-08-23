import pulp
import sys
from leer_archivos import abrir_y_leer_archivo
from backtracking import *

def defensa_tribu_agua_pl_aproximacion(maestros, k):
    n = len(maestros)
    problema = pulp.LpProblem("Crear_subgrupos", pulp.LpMinimize)

    # Definicion de variables de decision
    m = pulp.LpVariable.dicts("m", ((i, j) for i in range(k) for j in range(n)), 0, 1, pulp.LpBinary)

    # Restricciones
    # No se pueden repetir maestros entre los subgrupos
    for j in range(n):
        problema += pulp.lpSum(m[i, j] for i in range(k)) == 1

    # Ningun subgrupo puede quedar vacio
    for i in range(k):
        problema += pulp.lpSum(m[i, j] for j in range(n)) >= 1

    # Funcion objetivo
    Z = pulp.lpSum(m[i, j] * maestros[j][1] for i in range(k) for j in range(n))
    Y = pulp.lpSum(m[i, j] * maestros[j][1] for i in range(k) for j in range(n))
    problema += Z - Y

    problema.solve()
    
    subgrupos = [[] for _ in range(k)]
    for j in range(n):
        for i in range(k):
            if pulp.value(m[i, j]) == 1:
                subgrupos[i].append(maestros[j])

    suma = suma_cuadratica(subgrupos)

    return suma, subgrupos

def main():
    if len(sys.argv) < 2:
        print("Error: Uso 'python aproximacion_programacion_lineal.py <nombre_del_archivo.txt>'")
        sys.exit(1)
   
    ruta_archivo = sys.argv[1]
    k, maestros_agua = abrir_y_leer_archivo(ruta_archivo)
    suma_bt, _ = defensa_tribu_agua_backtracking(maestros_agua, k)
    suma_aprox, subgrupos = defensa_tribu_agua_pl_aproximacion(maestros_agua, k)
    
    i = 1
    for subgrupo in subgrupos:
        print(f"Grupo {i}: " + ', '.join([maestro[0] for maestro in subgrupo]))
        i += 1
    print("Coeficiente:", suma_aprox)
    
    print("Relacion de la aproximación con el óptimo:", (suma_aprox / suma_bt))

if __name__ == "__main__":
    main()
