pot=1
re=0
op=None
suma=0

while pot>0 and pot<31:
    op=10**pot
    re=0+op
    pot=pot+1
    suma=suma+re
    print('Las primeras treinta potencias de 10 son:',re)
print('La suma de las primeras 30 potencias de 10 es:',suma)
