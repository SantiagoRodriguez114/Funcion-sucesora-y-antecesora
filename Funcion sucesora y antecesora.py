#Funcion sucesora
def S(n):
    return n + 1


#Funcion antecesora
def A(n):
    return n - 1 if n > 0 else 0


def suma(a,b):
    if a < 0 or b < 0:
        return "Error"
    
    res = a
    
    for i in range(b):
        res = S(res)
        
    return res


def resta(a,b):
    if a < 0 or b < 0:
        return "Error"
        
    res = a
    
    for a in range(b):
        res = A(res)

    return res
    


def multiplicacion(a,b):
    if a < 0 or b < 0:
        return "Error"
    if a == 0 or b == 0:
        return 0
    
    res = 0
    
    for i in range (b):
        res = suma(res,a) 
        
        
    
    return res
    

def division(a, b):
    
    if a < 0 or b < 0:
        return "Error"

    if b == 0:
        return "Error: No se puede dividir por cero."

    cociente = 0
    dividendo = a 

    while dividendo >= b:
        dividendo = resta(dividendo, b)
        cociente += 1

    return cociente


#Pruebas 

print(suma(4,2))
print(resta(10,5))
print(multiplicacion(5,3))
print(division(4,2))
