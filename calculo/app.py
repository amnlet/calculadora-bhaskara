import math

def bhaskara_calc(a: int, b: int, c: int) -> int:
    delta = math.sqrt(b*b-4*a*c)
    if(delta < 0):
        print("Não existe raiz para essa função")
    else:
        result1 = -b+delta
        result1 = int(result1)/2*a
        result2 = -b-delta
        result2 = int(result2)/2*a
    return print(f"Resultado x¹: {result1} e x²: {result2}")

print(bhaskara_calc(a=1,b=2,c=-24))







