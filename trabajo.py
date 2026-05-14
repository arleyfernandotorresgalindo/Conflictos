def primo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    
    return True

def sumar(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma 
def hola(s):
    print f'Hola {s}'

def producto(L):
    r = 1
    for i in L:
        r *= i
    return r
def despedirse(s):
    return f'Hasta luego {s}'

def tabla_cinco(n):
    return 5*n
