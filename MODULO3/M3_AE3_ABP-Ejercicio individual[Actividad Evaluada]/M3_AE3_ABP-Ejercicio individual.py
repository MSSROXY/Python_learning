print('~~~ Bienvenido al sistema de pago ~~~')

dia_promocional = input('Confirma si es día promocional, escriba "SI" o "NO": ').upper()
print(dia_promocional)

productos = int(input('Ingresa la cantidad de productos a comprar: '))
print(productos)

cliente_frecuente = input('Confirma si es cliente frecuente, escriba "SI" o "NO": ').upper()
print(cliente_frecuente)

dolares = int(input('Ingresa el monto en dólares: '))
print(dolares)

print('***************')

descuento = 0

if dia_promocional == 'SI':
    descuento += 0.15
    print('Obtienes un 15% de descuento adicional por ser día promocional')
if productos > 10:
    if descuento < 0.30:
        descuento += 0.10
        print('Obtienes un 10% de descuento al comprar más de 10 productos')
    else:
        descuento +=0
if cliente_frecuente == 'SI':
    if descuento < 0.30:
        descuento += 0.05
        print('Obtienes un 5% de descuento por ser cliente frecuente')
    else:
        descuento +=0
if dolares > 500:
    if descuento < 0.30:
        descuento +=0.07
        print('Obtienes un 7% de descuento por compras sobre 500 dólares')
    else:
        descuento +=0
else:
    descuento +=0
    print('No aplica ningún descuento')

print('***************')
print('El total de la compra es:', dolares * (1 - descuento), 'dólares. Ahorraste un', descuento, '% en esta compra.')
