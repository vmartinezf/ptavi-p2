#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import csv
from calcoohija import CalculadoraHija
from calcoohija import numerical_float
from calcplus import resultados_fichero


def main():
    pass


if __name__ == "__main__":
    fichero = sys.argv[1]
    with open(fichero) as fich:
        resultados_fichero(fich)
