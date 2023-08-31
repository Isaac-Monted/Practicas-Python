#Ejercicio 1#

def comparacion():
    num = int(input('Escribe un numero: '))
    num2 = int(input('Escribe otro numero: '))
    if num < num2:
        return -1
    elif num > num2:
        return 1
    else:
        return 0
print('Escriba dos numeros para comparar')
print(comparacion())

#Ejercicio 2#
def factura():
    iva = 21
    cantidad = float(input('Escride la cantidad de la factura si IVA: '))
    iva = int(input('Escribe el valor del IVA: '))
    if iva != 0:
        if iva > 0:
            total = (cantidad * (iva / 100)) + cantidad
            return total
        else:
            return 'El IVA es negativo'
    else:
        total = (cantidad * 0.21) + cantidad
        return total

print('Ingresa una cantidad a facturar')
print('El total de su monto es:',factura())
