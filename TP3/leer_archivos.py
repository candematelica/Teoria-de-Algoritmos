def abrir_y_leer_archivo(ruta_archivo):
    try:
        archivo = open(ruta_archivo)
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {ruta_archivo}")
        return
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return
    next(archivo) # Me salto el encabezado

    grupos_a_formar = int(archivo.readline().strip())
    maestros_agua = []
    for linea in archivo:
        maestro , habilidad = linea.split(',')
        maestros_agua.append([maestro,int(habilidad)])
            
    
    archivo.close()
    return grupos_a_formar, maestros_agua
