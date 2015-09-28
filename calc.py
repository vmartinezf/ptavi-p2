#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys


def main():
    pass


#convierto el operando sea int o float a float
def numerical_float(operando):
    return float(operando)


def suma(sum1, sum2):
    return sum1 + sum2


def resta(rest1, rest2):
    return rest1 - rest2


if __name__ == "__main__":
    numero1 = sys.argv[1]
    operacion = sys.argv[2]
    numero2 = sys.argv[3]

    try:
        num1 = numerical_float(numero1)
        num2 = numerical_float(numero2)
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    if (operacion == "suma"):    
        print (suma(num1, num2))
    elif (operacion == "resta"):
        print (resta(num1, num2))
