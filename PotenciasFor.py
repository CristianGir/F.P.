pot=1
re=0
op=None
suma=0
l=list(range(0,30))

for i in l:
    op=10**pot
    re=0+op
    pot=pot+1
    suma=suma+re
    print('Las primeras treinta potencias de 10 son:',re)
print('La suma de las primeras 30 potencias de 10 es:',suma)
