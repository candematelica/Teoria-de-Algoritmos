import sys
import csv

def abrir_y_leer_archivo(nombre):
    texto_por_tuplas = []
    try:
        with open(nombre, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            # Saltamos la primera línea si contiene encabezados
            next(lector_csv, None)
            i = 0
            for linea in lector_csv:
                tupla = (i, int(linea[0]), int(linea[1])) # Convertimos a int los valores
                texto_por_tuplas.append(tupla)
                i += 1
            return texto_por_tuplas
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {nombre}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def orden_de_las_batallas(batallas):
    batallas_ord = sorted(batallas, key=lambda x: x[1] / x[2]) # Ordenar por la proporción
    F = 0
    suma_total = 0

    for i in range(len(batallas_ord)):
        F += batallas_ord[i][1]
        suma_total += F * batallas_ord[i][2]

    return batallas_ord, suma_total

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <nombre_del_archivo.txt>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    batallas = abrir_y_leer_archivo(nombre_archivo)
    batallas_ord, suma_total = orden_de_las_batallas(batallas)
    print(batallas_ord)
    print(suma_total)
    
if __name__ == "__main__":
    main()
