#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys


# convierto el operando sea int o float a float
def numerical_float(operando):
    return float(operando)


def suma(sum1, sum2):
    return sum1 + sum2


def resta(rest1, rest2):
    return rest1 - rest2


def resultado(operacion, num1, num2):
    if (operacion == "suma"):
        result = suma(num1, num2)
    elif (operacion == "resta"):
        result = resta(num1, num2)
    else:
        sys.exit("Error: the operation is incorrect")
    return result


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
