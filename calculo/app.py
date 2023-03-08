import math

class Calculo():
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c

    def delta_bhaskara(a,b,c):
        deltaint = b*b-4*a*c
        delta = math.sqrt(deltaint)
        r1 = -b+delta
        r2 = -b-delta
        r3 = 2*a
        result = [r1,r2]
        result1 = []
        if delta < 0:
            print("Não possui raizes.")
        else:
            result1.append(list(map(lambda x: x/r3, result)))
            for respostas in result1:
                list(respostas)
                print(f"Delta: {delta}\nx¹: {respostas[0]}\nx²: {respostas[1]}")                
if(__name__ == "__main__"):
    Calculo.delta_bhaskara(1,-10,0)