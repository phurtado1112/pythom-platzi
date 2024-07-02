a = [1, 2, 3, 4, 5]

b = a

print('Valores de a: ', a)
print('Valores de b: ', b)
print('')

print('++++++++++ elimina el elemento 1 +++++++++')

del a[0]

print('Nuevos Valores de a: ', a)
print('Nuevos Valores de b: ', b)
print('')

print('++++++++++ identificación de espacio en memoria +++++++++')

print('Espacio de memoria de a ', id(a))
print('Espacio de memoria de b ', id(b))
print('')

print('++++++++++ utilizando slice +++++++++')

c = a[:]

print(c)
print('Espacio de memoria de c ', id(c))
print('')

print('++++++++++ se agrega el valor 5 a "a"  +++++++++')

a.append(6)

print(a)
print(b)
print(c)
print('')