import sys 

def factorialRecursive(n):
    if n == 1:
        return n
    return n*factorial(n-1)

def factorial(n):
    i = 1
    for f in range(1, n+1):
        i = i * f
    return i

if __name__ == '__main__':
    print ("Factorial Recursive: {}".format(factorialRecursive(int(sys.argv[1]))))
    print ("Factorial : {}".format(factorial(int(sys.argv[1]))))
