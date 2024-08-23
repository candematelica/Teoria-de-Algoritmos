import sys

ATACAR =  "Atacar"
CARGAR = "Cargar"

def abrir_y_leer_archivo(ruta_archivo):
    try:
        archivo = open(ruta_archivo)
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {archivo}")
        return
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return
    next(archivo) # Me salto el encabezado

    i = 0
    minutos = 0
    enemigos = []
    recarga = []
    for linea in archivo:
        num = int(linea.strip())
        if i == 0:
            minutos = num
        elif i <= minutos:
            enemigos.append(num)
        else:
            recarga.append(num)
        i += 1
    
    archivo.close()
    return enemigos, recarga

def ataques_da_li(enemigos, recarga):
    n = len(enemigos)
    OPT = [0] * (n + 1)
    recarga_usada = [0] * (n + 1)

    for i in range(1, n + 1):
        OPT[i] = OPT[i - 1]
        for r in range(1, i + 1):
            opt_actual = OPT[i]
            OPT[i] = max(opt_actual, OPT[i - r] + min(enemigos[i - 1], recarga[r - 1]))
            if OPT[i] != opt_actual:
                recarga_usada[i] = r
    
    # Reconstruccion de la solucion
    secuencia_ataques = [CARGAR] * n
    i = n
    while i > 0:
        if recarga_usada[i] == 0:
            i -= 1
        else:
            secuencia_ataques[i - 1] = ATACAR
            i -= recarga_usada[i]

    return OPT[n], secuencia_ataques

def main():
    if len(sys.argv) < 2:
        print("Error: Uso 'python main.py <nombre_del_archivo.txt>'")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    enemigos, recarga = abrir_y_leer_archivo(ruta_archivo)
    eliminados, secuencia_ataques = ataques_da_li(enemigos, recarga)
    print("Estrategia: " + ", ".join(str(ataque) for ataque in secuencia_ataques))
    print("Cantidad de tropas eliminadas:", eliminados)

if __name__ == "__main__":
    main()
