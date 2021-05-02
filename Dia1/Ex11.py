import math

tp1 = float(input("TP1: "))
tp2 = float(input("TP2: "))
ep = float(input("EP: "))

t = (tp1*0.40) + (tp2*0.60) #Verificação da componente teórica isolada

if t < 7.5:
    print("Reprovado por nota mínima na teórica: %.1f"%t )
elif ep < 7.5:
    print("Reprovado por nota mínima na prática: %.1f"%ep )
else: 
    nf = (tp1 * 0.2) + (tp2 * 0.3) + (ep * 0.5)
    if nf < 9.5:
        print("Reprovado. Nota: %.1f"%nf)
    elif nf == 9.5:
        print("Aprovado. Nota: 10.0")
    else :
        print("Aprovado. Nota: %.1f"%nf)
