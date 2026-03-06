#!/usr/bin/env python3
"""
Calculadora Multi-Base
Soporta operaciones en binario, octal y hexadecimal.
Python 3.11+
"""

import os
import sys
from typing import Callable


# ==========================
# UTILIDADES VISUALES
# ==========================

def limpiar_pantalla() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pausar() -> None:
    input("\nPresiona ENTER para continuar...")


def banner() -> None:
    print("\033[96m")
    print("=" * 55)
    print("      🧮  CALCULADORA MULTI-BASE PRO  🧮")
    print("=" * 55)
    print("\033[0m")


# ==========================
# CONVERSIÓN
# ==========================

BASES = {
    "1": ("Binario", 2),
    "2": ("Octal", 8),
    "3": ("Hexadecimal", 16),
}


def convertir_a_decimal(valor: str, base: int) -> int:
    return int(valor, base)


def convertir_desde_decimal(valor: int, base: int) -> str:
    if base == 2:
        return bin(valor)
    elif base == 8:
        return oct(valor)
    elif base == 16:
        return hex(valor)
    else:
        return str(valor)


# ==========================
# OPERACIONES
# ==========================

OPERACIONES: dict[str, tuple[str, Callable[[int, int], float]]] = {
    "1": ("Suma", lambda a, b: a + b),
    "2": ("Resta", lambda a, b: a - b),
    "3": ("Multiplicación", lambda a, b: a * b),
    "4": ("División", lambda a, b: a / b),
}


# ==========================
# MENÚS
# ==========================

def menu_principal() -> str:
    print("\nSelecciona el sistema numérico:")
    for key, (nombre, _) in BASES.items():
        print(f"  {key}. {nombre}")
    print("  0. Salir")
    return input("\n👉 Opción: ")


def menu_operaciones() -> str:
    print("\nSelecciona la operación:")
    for key, (nombre, _) in OPERACIONES.items():
        print(f"  {key}. {nombre}")
    return input("\n👉 Opción: ")


# ==========================
# LÓGICA PRINCIPAL
# ==========================

def ejecutar_calculadora() -> None:
    while True:
        limpiar_pantalla()
        banner()

        opcion_base = menu_principal()

        if opcion_base == "0":
            print("\n👋 Saliendo del sistema...")
            sys.exit()

        if opcion_base not in BASES:
            print("\n❌ Opción inválida.")
            pausar()
            continue

        nombre_base, base = BASES[opcion_base]

        opcion_operacion = menu_operaciones()

        if opcion_operacion not in OPERACIONES:
            print("\n❌ Operación inválida.")
            pausar()
            continue

        nombre_operacion, operacion = OPERACIONES[opcion_operacion]

        try:
            print(f"\nSistema seleccionado: {nombre_base}")
            a = input("Ingresa el primer número: ")
            b = input("Ingresa el segundo número: ")

            decimal_a = convertir_a_decimal(a, base)
            decimal_b = convertir_a_decimal(b, base)

            if nombre_operacion == "División" and decimal_b == 0:
                raise ZeroDivisionError

            resultado = operacion(decimal_a, decimal_b)

            limpiar_pantalla()
            banner()
            print(f"\n📌 Resultado de {nombre_operacion}")
            print("-" * 40)

            if nombre_operacion == "División":
                print(f"Decimal: {resultado}")
            else:
                resultado = int(resultado)
                print(f"En {nombre_base}: {convertir_desde_decimal(resultado, base)}")
                print(f"Binario: {bin(resultado)}")
                print(f"Octal: {oct(resultado)}")
                print(f"Hexadecimal: {hex(resultado)}")
                print(f"Decimal: {resultado}")

        except ValueError:
            print("\n❌ Error: número inválido para esa base.")
        except ZeroDivisionError:
            print("\n❌ Error: división por cero.")
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")

        pausar()


# ==========================
# ENTRY POINT
# ==========================

if __name__ == "__main__":
    ejecutar_calculadora()
