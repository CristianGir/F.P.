#Leer 3 números enteros, y leer uno adicional "1" para > y "2" para <.
print('Se van a comparar tres números y se van a organizar según la elección.')
v=int(input('Ingrese "1" para organizarlo de mayor a menor, \
o "2" para organizarlos de menor a mayor: '))
while v!=1 and v!=2:
    v=int(input('Por favor seleccione una opción válida, "1" >, "2"<: '))
A=int(input('Ingrese el número A: '))
B=int(input('Ingrese el número B: '))
C=int(input('Ingrese el número C: '))
if v==1:
    if A==B:
        print('A y B son iguales a: ',A)
        if A>C:
            print(C)
    elif A==C:
        print('A y C son iguales a: ',A)
        if C>B:
            print(B)
    elif C==B:
        print('C y B son iguales a: ',C)
        if C>A:
            print(A)
    elif A>B and A>C:
        print(A)
        if B>C:
            print(B)
            print(C)
        else:
            print(C)
            print(B)
    elif B>A and B>C:
        print(B)
        if A>C:
            print(A)
            print(C)
        else:
            print(C)
            print(A)
    elif C>A and C>B:
        print(C)
        if A>B:
            print(A)
            print(B)
        else:
            print(B)
            print(A)
    elif A==B and A==C:
        print('Los tres números son iguales.')
            
#División entre mayor y menor.
            
elif v==2:
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
    elif A==B and A==C:
        print('Los tres números son iguales.')
    
    elif A==B:
        print('A y B son iguales a: ',A)
        if A<C:
            print(C)
        else:
            print(C)
    elif A==C:
        print('A y C son iguales a: ',A)
        if C<B:
            print(B)
        else:
            print(B)
    elif C==B:
        print('C y B son iguales a: ',C)
        if C<A:
            print(A)
        else:
            print(A)
