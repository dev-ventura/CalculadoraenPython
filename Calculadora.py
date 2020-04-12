#Calculadora por consola (Debe sumar, restar, multiplicar y dividir 2 números, Tener menú de opciones)
def suma(nump,numq):
    res=nump+numq
    print(res)
def resta(nump,numq):
    res=nump-numq
    print(res)
def multiplicacion(nump,numq):
    res=nump*numq
    print(res)
def division(nump, numq):
    res=nump/numq
    resmod=nump%numq
    print(res)
print('Ingrese dos numeros')
print('Ingrese el primer numero:')
a=int(input())
print('Ingrese el siguiente numero:')
b=int(input())
print('Menu de opciones')
print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Division')

print('Que operacion desea realizar:')
opcion=int(input())
operaciones=[1,2,3,4]
if (operaciones[0]==opcion):
    print('El resultado es:')
    resultado=suma(a,b)
elif (operaciones[1]==opcion):
    print('El resultado es:')
    resultado=resta(a,b)
elif (operaciones[2]==opcion):
    print('El resultado es:')
    resultado=multiplicacion(a,b)
elif (operaciones[3]==opcion):
    print('El resultado es:')
    resultado=division(a,b)
else:
    print('Esa opcion no existe, digite nuevamente')