#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys


class Calculadora():

    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2


class CalculadoraHija(Calculadora):
    def multiplicacion(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):  
        try:
            return num1 / num2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")


def main():
    pass


#convierto el operando sea int o float a float
def numerical_float(operando):
    return float(operando)


def resultado(operacion, num1, num2):
    result = CalculadoraHija()
    if (operacion == "suma"):    
        total = result.suma(num1, num2)
    elif (operacion == "resta"):
        total = result.resta(num1, num2)
    elif (operacion == "multiplica"):
        total = result.multiplicacion(num1, num2)
    elif (operacion == "divide"):
        total = result.division(num1, num2)
    else:
        sys.exit ("Error: the operation is incorrect")
    return total


if __name__ == "__main__":
    try:
        numero1 = sys.argv[1]
        operacion = sys.argv[2]
        numero2 = sys.argv[3]
    except IndexError:
        sys.exit("Error: The number of parameters is incorrect")
    try:
        num1 = numerical_float(numero1)
        num2 = numerical_float(numero2)
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    print (resultado(operacion, num1, num2))
