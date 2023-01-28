import math
import sys

res = math.factorial(int(sys.argv[1])) + math.factorial(int(sys.argv[2])) 
print("La suma de " + sys.argv[1] + "! + " + sys.argv[2] + "! = " + str(res))
