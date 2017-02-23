from math import sqrt

PHI = 1.61803398875
SQRT_5 = sqrt(5)

print(SQRT_5)

# Based on
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
def fibo_index(n):
    return (int) ( (pow(PHI, n) - (-pow(PHI,-n))) / SQRT_5
            )

index = 3 #Third value in fibonacci sequence is even, 6, 9 are and so forth
suma  = 0
while True:
    fibo = fibo_index(index)
    if fibo > 4000000:
        break
    suma += fibo
    index += 3

print("Sum is {}".format(suma))
