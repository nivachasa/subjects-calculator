def ingresar_calificaciones():
    materias = []
    calificaciones = []
    
    print("INGRESO DE MATERIAS Y CALIFICACIONES")
    
    while True:
        # Solicitar nombre de la materia
        materia = input("\nIngrese el nombre de la materia (o 'salir' para terminar): ").strip()
        
        if materia.lower() == 'salir':
            break
        
        if not materia:
            print("Error: El nombre de la materia no puede estar vacío. Intente nuevamente.")
            continue
        
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para {materia} (0-10): "))
                
                if calificacion < 0 or calificacion > 10:
                    print("Error: La calificación debe estar entre 0 y 10. Intente nuevamente.")
                    continue
                
                materias.append(materia)
                calificaciones.append(calificacion)
                print(f"✓ {materia}: {calificacion} registrado exitosamente")
                break
                
            except ValueError:
                print("Error: Ingrese un número válido. Intente nuevamente.")
    
    return materias, calificaciones


def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    return promedio


def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []
    
    for indice, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(indice)
        else:
            reprobadas.append(indice)
    
    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    if len(calificaciones) == 0:
        return None, None
    
    indice_maxima = calificaciones.index(max(calificaciones))
    indice_minima = calificaciones.index(min(calificaciones))
    
    return indice_maxima, indice_minima


def mostrar_resumen(materias, calificaciones):
    print("RESUMEN DE CALIFICACIONES")
    
    # Verificar si hay materias ingresadas
    if len(materias) == 0:
        print("\n⚠ No se ingresaron materias. Programa finalizado.")
        return
    
    # Mostrar todas las materias con sus calificaciones
    print("\n📋 MATERIAS Y CALIFICACIONES:")
    for indice, (materia, calificacion) in enumerate(zip(materias, calificaciones), 1):
        print(f"{indice}. {materia}: {calificacion}")
    
    # Calcular y mostrar promedio general
    promedio = calcular_promedio(calificaciones)
    print(f"📊 PROMEDIO GENERAL: {promedio:.2f}")
    
    # Determinar y mostrar aprobadas/reprobadas
    aprobadas, reprobadas = determinar_estado(calificaciones)
    
    print("\n✅ MATERIAS APROBADAS:")
    if aprobadas:
        for indice in aprobadas:
            print(f"   • {materias[indice]}: {calificaciones[indice]}")
    else:
        print("   Ninguna materia aprobada")
    
    print("\n❌ MATERIAS REPROBADAS:")
    if reprobadas:
        for indice in reprobadas:
            print(f"   • {materias[indice]}: {calificaciones[indice]}")
    else:
        print("   Ninguna materia reprobada")
    
    # Encontrar y mostrar extremos
    indice_maxima, indice_minima = encontrar_extremos(calificaciones)
    
    print(f"🏆 MEJOR CALIFICACIÓN: {materias[indice_maxima]} con {calificaciones[indice_maxima]}")
    print(f"📉 PEOR CALIFICACIÓN: {materias[indice_minima]} con {calificaciones[indice_minima]}")



def main():
    print("\n╔════════════════════════════════════════════╗")
    print("║  CALCULADORA DE PROMEDIOS ESCOLARES        ║")
    print("╚════════════════════════════════════════════╝")

    materias, calificaciones = ingresar_calificaciones()
    
    print("\n")
    print("Listado de materias:", materias) 
    print("Listado de calificaciones:", calificaciones)
    print("\n")

    mostrar_resumen(materias, calificaciones)
    
    print("\n╔════════════════════════════════════════════╗")
    print("║  ¡Gracias por usar la calculadora!👋       ║")
    print("║  ¡Éxito en tus estudios! 📚                ║")
    print("╚════════════════════════════════════════════╝\n")



if __name__ == "__main__":
    main()
