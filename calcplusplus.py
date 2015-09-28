#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import csv
from calcoohija import CalculadoraHija
from calcoohija import numerical_float


def main():
    pass


if __name__ == "__main__":
    fichero = sys.argv[1]
    with open(fichero) as fich:
        lines = fich.readlines()
        for line in lines:
            lineas = line.split()
            for operandos in lineas:
                operando = operandos.split(',')
                operacion = operando[0]
                numero = numerical_float(operando[1])
                result = CalculadoraHija()
                for i in operando[2:]:
                    number = int(i)
                    num2 = numerical_float(number)     
                    if (operacion == "suma"):   
                        numero = result.suma(numero, num2)
                    elif (operacion == "resta"):
                        numero = result.resta(numero, num2)
                    elif (operacion == "multiplica"):
                        numero = result.multiplicacion(numero, num2)
                    elif (operacion == "divide"):
                        numero = result.division(numero, num2)
                print (numero)             
