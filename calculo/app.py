import math

def calc(a,b,c):
    delta = b*b-4*a*c
    deltaint = int(delta)
    raizDelta = math.sqrt(deltaint)
    baskhara1 = -b+int(raizDelta)/2*a
    baskhara2 = -b-int(raizDelta)/2*a
    if deltaint < 0:
        print("NÃO EXISTEM RAIZES PARA ESSA FUNÇÃO")
    elif deltaint == float:
        deltaint = int(deltaint)
    else:
        return print(f"Delta: {deltaint}\nRaiz de Delta: {int(raizDelta)}\nResultado: X¹= {baskhara1} X²= {baskhara2}")


print(calc(1,2,-24))