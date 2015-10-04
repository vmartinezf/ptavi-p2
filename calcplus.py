#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from calcoohija import CalculadoraHija
from calcoohija import numerical_float
from calcoohija import resultado


def main():
    pass


def resultados_operaciones(lineas):
    for operandos in lineas:
            operando = operandos.split(',')
            operacion = operando[0]
            numero = numerical_float(operando[1])
            for i in operando[2:]:
                number = int(i)
                num2 = numerical_float(number)
                total = resultado(operacion, numero, num2)
                numero = numerical_float(total)
    return total


def lineas_fichero(lines):
    for line in lines:
        lineas = line.split()
        total = resultados_operaciones(lineas)
        print (total)


def resultados_fichero(fich):
    lines = fich.readlines()
    lineas_fichero(lines)


if __name__ == "__main__":
    fichero = sys.argv[1]
    fich = open(fichero, 'r')
    resultados_fichero(fich)
    fich.close()
