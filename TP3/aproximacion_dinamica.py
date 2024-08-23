from leer_archivos import abrir_y_leer_archivo
import sys
from backtracking import defensa_tribu_agua_backtracking

def algoritmo_aproximacion_dinamica(maestros, k):
    n = len(maestros)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    particiones = [[-1] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    sumas_acumuladas = [0] * (n + 1)
    for i in range(1, n + 1):
        sumas_acumuladas[i] = sumas_acumuladas[i - 1] + maestros[i - 1][1]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for m in range(i):
                suma_grupo = sumas_acumuladas[i] - sumas_acumuladas[m]
                costo = dp[m][j - 1] + suma_grupo ** 2
                if costo < dp[i][j]:
                    dp[i][j] = costo
                    particiones[i][j] = m
    grupos = []
    i, j = n, k
    while j > 0:
        m = particiones[i][j]
        grupos.append(maestros[m:i])
        i, j = m, j - 1
    
    grupos.reverse()
    return dp[n][k], grupos

def main():
    if len(sys.argv) < 2:
        print("Error: Uso 'python aproximacion_dinamica.py <nombre_del_archivo.txt>'")
        sys.exit(1)
   
    ruta_archivo = sys.argv[1]
    k, maestros_agua = abrir_y_leer_archivo(ruta_archivo)
    suma_bt, _ = defensa_tribu_agua_backtracking(maestros_agua, k)
    suma_aprox, subgrupos = algoritmo_aproximacion_dinamica(maestros_agua, k)
    
    i = 1
    for subgrupo in subgrupos:
        print(f"Grupo {i}: " + ', '.join([maestro[0] for maestro in subgrupo]))
        i += 1
    print("Coeficiente:", suma_aprox)
    
    print("Relacion de la aproximación con el óptimo:", (suma_aprox / suma_bt))

if __name__ == "__main__":
    main()
