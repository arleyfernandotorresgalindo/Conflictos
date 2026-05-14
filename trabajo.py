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