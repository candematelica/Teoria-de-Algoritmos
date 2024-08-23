from leer_archivos import abrir_y_leer_archivo
import sys

def suma_cuadratica(subgrupos):
    return sum(sum(maestro[1] for maestro in subgrupo) ** 2 for subgrupo in subgrupos)

def _defensa_tribu_agua_backtracking(maestros, k, subgrupos, mejor_suma, mejor_solucion, i):
    if i >= len(maestros):
        suma_actual = suma_cuadratica(subgrupos)
        if suma_actual < mejor_suma:
            return suma_actual, [list(subgrupo) for subgrupo in subgrupos]
        return mejor_suma, mejor_solucion
    
    for j in range(k):
        subgrupos[j].append(maestros[i])
        if (len(subgrupos[j]) - 1) <= (len(maestros) - k):
            mejor_suma, mejor_solucion = _defensa_tribu_agua_backtracking(maestros, k, subgrupos, mejor_suma, mejor_solucion, i + 1)
        subgrupos[j].pop()
    
    return mejor_suma, mejor_solucion

def defensa_tribu_agua_backtracking(maestros, k):
    maestros.sort(key=lambda x: x[1], reverse=True)
    return _defensa_tribu_agua_backtracking(maestros, k, [[] for _ in range(k)], float("inf"), [], 0)

def main():
    if len(sys.argv) < 2:
        print("Error: Uso 'python backtracking.py <nombre_del_archivo.txt>'")
        sys.exit(1)
   
    ruta_archivo = sys.argv[1]
    k, maestros_agua = abrir_y_leer_archivo(ruta_archivo)
    suma, subgrupos = defensa_tribu_agua_backtracking(maestros_agua, k)
    
    i = 1
    for subgrupo in subgrupos:
        print(f"Grupo {i}: " + ', '.join([maestro[0] for maestro in subgrupo]))
        i += 1
    print("Coeficiente:", suma)

if __name__ == "__main__":
    main()
