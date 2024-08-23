from leer_archivos import abrir_y_leer_archivo
from backtracking import *
import sys

def algoritmo_aproximacion_greedy(maestros_agua, k):
    subgrupos = [[] for _ in range(k)]
    maestros_ordenados = sorted(maestros_agua, key=lambda x: x[1], reverse=True)
    
    for maestro in maestros_ordenados:
        min = sum(maestro[1] for maestro in subgrupos[0]) ** 2
        min_pos = 0
        
        for i in range(1, k):
            cuadrado_suma = sum(maestro[1] for maestro in subgrupos[i]) ** 2
            if min > cuadrado_suma:
                min = cuadrado_suma
                min_pos = i
        
        subgrupos[min_pos].append(maestro)

    suma = suma_cuadratica(subgrupos)
    
    return suma, subgrupos
    
def main():
    if len(sys.argv) < 2:
        print("Error: Uso 'python aproximacion_greedy.py <nombre_del_archivo.txt>'")
        sys.exit(1)
   
    ruta_archivo = sys.argv[1]
    k, maestros_agua = abrir_y_leer_archivo(ruta_archivo)
    suma_bt, _ = defensa_tribu_agua_backtracking(maestros_agua,k)
    suma_aprox, subgrupos = algoritmo_aproximacion_greedy(maestros_agua, k)
    
    i = 1
    for subgrupo in subgrupos:
        print(f"Grupo {i}: " + ', '.join([maestro[0] for maestro in subgrupo]))
        i += 1
    print("Coeficiente:", suma_aprox)
    
    print("Relacion de la aproximación con el óptimo:", (suma_aprox / suma_bt))

if __name__ == "__main__":
    main()
