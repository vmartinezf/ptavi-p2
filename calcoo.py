#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys

class Calculadora():

    def suma (self,num1, num2):
        return num1 + num2

    def resta (self,num1, num2):
    	return num1 - num2

def main():
    pass

#convierto el operando sea int o float a float
def numerical_float (operando):
    return float(operando)

if __name__ == "__main__":

    numero1 = sys.argv[1]
    operacion = sys.argv[2]
    numero2 = sys.argv[3]

    try:
        num1 = numerical_float (numero1)
        num2 = numerical_float (numero2)
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    result = Calculadora()
    if (operacion == "suma"):    
        print (result.suma(num1, num2))
    elif (operacion == "resta"):
        print(result.resta(num1, num2))
        
