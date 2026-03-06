# Programa para analizar si una relación es reflexiva, simétrica y transitiva

def es_reflexiva(conjunto, relacion):
    for elemento in conjunto:
        if (elemento, elemento) not in relacion:
            return False
    return True


def es_simetrica(relacion):
    for (a, b) in relacion:
        if (b, a) not in relacion:
            return False
    return True


def es_transitiva(relacion):
    for (a, b) in relacion:
        for (c, d) in relacion:
            if b == c and (a, d) not in relacion:
                return False
    return True


def ingresar_relacion():
    conjunto = input("Ingrese los elementos del conjunto separados por coma: ").split(",")
    conjunto = [x.strip() for x in conjunto]

    relacion = set()
    n = int(input("¿Cuántos pares ordenados tendrá la relación?: "))

    for i in range(n):
        a = input(f"Ingrese el primer elemento del par {i+1}: ")
        b = input(f"Ingrese el segundo elemento del par {i+1}: ")
        relacion.add((a, b))

    return conjunto, relacion


def analizar_relacion(conjunto, relacion):
    print("\n--- RESULTADOS ---")

    if es_reflexiva(conjunto, relacion):
        print("La relación ES reflexiva")
    else:
        print("La relación NO es reflexiva")

    if es_simetrica(relacion):
        print("La relación ES simétrica")
    else:
        print("La relación NO es simétrica")

    if es_transitiva(relacion):
        print("La relación ES transitiva")
    else:
        print("La relación NO es transitiva")


def menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Ingresar relación")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            conjunto, relacion = ingresar_relacion()
            analizar_relacion(conjunto, relacion)

        elif opcion == "2":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")


menu()