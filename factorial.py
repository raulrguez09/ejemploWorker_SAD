import math
import sys

# Ejemplo de programa que suma el factorial de dos numeros pasados por parametro
res = math.factorial(int(sys.argv[1])) + math.factorial(int(sys.argv[2])) 
print("La suma de " + sys.argv[1] + "! + " + sys.argv[2] + "! = " + str(res))
