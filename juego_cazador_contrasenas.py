"""
Fase 5 - Entrega proyecto de software
Juego: Cazador de Contrasenas
Origen: Daniela
Estudiante: Daniela Fernanda Aguirre Acosta
Curso: Programacion
Codigo: 213023
Grupo: 382

Este programa cumple la guia de aprendizaje:
- Usa Programacion Orientada a Objetos.
- Genera contrasenas aleatorias.
- Valida mayusculas, minusculas, numeros, caracteres especiales y no repetidos.
- Maneja excepciones personalizadas.
- Usa cofres con puntajes.
- Permite jugar varias rondas.
"""

from __future__ import annotations

import random
import string
from dataclasses import dataclass


class ErrorJuego(Exception):
    """Clase base para los errores controlados del juego."""


class LongitudInvalidaError(ErrorJuego):
    """Error cuando la longitud ingresada no cumple las condiciones."""


class DatoNoNumericoError(ErrorJuego):
    """Error cuando el usuario ingresa un dato no numerico."""


class ContrasenaInvalidaError(ErrorJuego):
    """Error cuando la contrasena generada no cumple las reglas."""


class Contrasena:
    """Clase encargada de generar y validar contrasenas."""

    MAYUSCULAS = string.ascii_uppercase
    MINUSCULAS = string.ascii_lowercase
    NUMEROS = string.digits
    ESPECIALES = "\u00bf\u00a1?=)(/\u00a8*+-%&$#!"
    CARACTERES = MAYUSCULAS + MINUSCULAS + NUMEROS + ESPECIALES

    def __init__(self, longitud: int) -> None:
        self.longitud = longitud
        self.valor = ""

    @staticmethod
    def validar_longitud(texto: str) -> int:
        """Convierte y valida la longitud ingresada por el usuario."""
        try:
            longitud = int(texto)
        except ValueError as exc:
            raise DatoNoNumericoError("Debe ingresar un numero entero.") from exc

        if longitud < 8:
            raise LongitudInvalidaError("La longitud minima es de 8 caracteres.")

        maximo = len(set(Contrasena.CARACTERES))
        if longitud > maximo:
            raise LongitudInvalidaError(
                f"La longitud maxima sin repetir caracteres es {maximo}."
            )

        return longitud

    def generar(self) -> str:
        """
        Genera una contrasena completamente aleatoria.

        Se usa random.sample para evitar caracteres repetidos y random.shuffle
        para que el orden final no sea predecible.
        """
        caracteres_disponibles = list(dict.fromkeys(self.CARACTERES))
        seleccionados = random.sample(caracteres_disponibles, self.longitud)
        random.shuffle(seleccionados)
        self.valor = "".join(seleccionados)
        return self.valor

    def validar(self) -> bool:
        """Valida que la contrasena cumpla todos los requisitos."""
        reglas = [
            len(self.valor) >= 8,
            len(set(self.valor)) == len(self.valor),
            any(caracter in self.MAYUSCULAS for caracter in self.valor),
            any(caracter in self.MINUSCULAS for caracter in self.valor),
            any(caracter in self.NUMEROS for caracter in self.valor),
            any(caracter in self.ESPECIALES for caracter in self.valor),
        ]

        if not all(reglas):
            raise ContrasenaInvalidaError(
                "La contrasena no cumple todos los requisitos de seguridad."
            )

        return True


@dataclass(frozen=True)
class Cofre:
    """Clase que representa los cofres y sus puntos."""

    nombre: str
    puntos: int

    @classmethod
    def aleatorio_valido(cls) -> "Cofre":
        """Devuelve un cofre positivo de forma aleatoria."""
        cofres = [
            cls("Comun", 10),
            cls("Raro", 25),
            cls("Legendario", 50),
        ]
        return random.choice(cofres)

    @classmethod
    def maldito(cls) -> "Cofre":
        """Devuelve el cofre que penaliza contrasenas invalidas."""
        return cls("Maldito", -20)


class JuegoCazador:
    """Clase que administra el puntaje, las rondas y el flujo del juego."""

    def __init__(self) -> None:
        self.puntaje = 0
        self.ronda = 1

    def mostrar_inicio(self) -> None:
        print("=" * 60)
        print("CAZADOR DE CONTRASENAS")
        print("=" * 60)
        print("Objetivo: generar contrasenas para abrir cofres.")
        print("Una contrasena valida abre un cofre positivo.")
        print("Una contrasena invalida abre un cofre maldito.")
        print()
        print("Reglas de la contrasena:")
        print("- Minimo 8 caracteres.")
        print("- Al menos una mayuscula.")
        print("- Al menos una minuscula.")
        print("- Al menos un numero.")
        print("- Al menos un caracter especial: ¿¡?=)(/¨*+-%&$#!")
        print("- No debe repetir caracteres.")

    def pedir_longitud(self) -> int:
        texto = input("\nIngrese la longitud de la contrasena: ").strip()
        return Contrasena.validar_longitud(texto)

    def jugar_ronda(self) -> None:
        print("\n" + "-" * 60)
        print(f"Ronda {self.ronda}")
        print("-" * 60)

        try:
            longitud = self.pedir_longitud()
            contrasena = Contrasena(longitud)
            valor = contrasena.generar()

            print(f"Contrasena generada: {valor}")
            contrasena.validar()

            cofre = Cofre.aleatorio_valido()
            print(f"Contrasena valida. Abriste un cofre {cofre.nombre}.")

        except ErrorJuego as error:
            cofre = Cofre.maldito()
            print(f"Error controlado: {error}")
            print("Abriste un cofre Maldito.")

        self.puntaje += cofre.puntos

        signo = "+" if cofre.puntos > 0 else ""
        print(f"Puntos de la ronda: {signo}{cofre.puntos}")
        print(f"Puntaje acumulado: {self.puntaje}")

        self.ronda += 1

    def desea_continuar(self) -> bool:
        respuesta = input("\nDesea jugar otra ronda? (s/n): ").strip().lower()
        return respuesta in {"s", "si", "sí"}

    def iniciar(self) -> None:
        self.mostrar_inicio()

        continuar = True
        while continuar:
            self.jugar_ronda()
            continuar = self.desea_continuar()

        print("\n" + "=" * 60)
        print("Juego finalizado.")
        print(f"Puntaje final: {self.puntaje}")
        print("=" * 60)


if __name__ == "__main__":
    juego = JuegoCazador()
    juego.iniciar()
