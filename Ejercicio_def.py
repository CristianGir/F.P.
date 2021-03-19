def cantidad(cad):
    cant=0
    for x in range(len(cad)):
        if cad[x]=='a' or cad[x]=='e' or cad[x]=='i' or cad[x]=='o' or cad[x]=='u':
            cant=cant+1
        print('La cantidad de vocales en',cad, 'es:',cant)
cantidad('aromaterapia')
cantidad('murcielago')
cantidad('olimpo')

#Segundo ejercicio.

def ordenar():
    if A<B and A<C:
        print(A)
        if B<C:
            print(B)
            print(C)
        else:
            print(C)
            print(B)
    elif B<A and B<C:
        print(B)
        if A<C:
            print(A)
            print(C)
        else:
            print(C)
            print(A)
    elif C<A and C<B:
        print(C)
        if A<B:
            print(A)
            print(B)
        else:
            print(B)
            print(A)

A=int(input('Ingrese el primer número: '))
B=int(input('Ingrese el segundo número: '))
C=int(input('Ingrese el tercer número: '))
ordenar()
