to_do = ['Dirgirnos al hotel', 'Ir a almorzar', 'Visitar un museo', 'Volver al hotel']

print(to_do)

numbers = [1, 2, 3 , 4, 'cinco']
print(numbers)
print(type(numbers))

print('+++++++++++++++++++ mix list +++++++++++++++++++')

mix = ['uno', 2, 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print('Primer elemento: ', mix[0])
print('Segundo elemento: ', mix[2])
print('ültimo elemento: ', mix[-1])

print('0:2')
print(mix[0:2])
print('0:4')
print(mix[0:4])
print('')

print('+++++++++++++++++++ extracción de elementos +++++++++++++++++++')

string = 'Hola mundo'

print('Primer elemento: ', string[0])
print('Segundo elemento: ', string[1])
print('')
print('ültimo elemento: ', string[-2])
print('ültimo elemento: ', string[-1])
print('')

print('+++++++++++++++++++ modicar la lista +++++++++++++++++++')
print('///////////////////// Agragar /////////////////////////')

print('mix ', mix)
print('')

mix.append(False)

print('mix después de append ', mix)
print('')

mix.append(['a', 'b'])

print('mix después del 2do append ', mix)
print('')

print('///////////////////// Insertar /////////////////////////')

mix.insert(1, ['c', 'd'])
print('mix después de insertar en la posicíon uno', mix)
print('')
print('Indice del elemento ["c", "d"] de la lista mix ', mix.index(['c', 'd']))
print('')

print('///////////////////// Verificaciones en la lista /////////////////////////')

numbers = [1, 2, 100, 90, 45, 3, 4, 5]
print('Lista de numbers ', numbers)
print('')
print('El mayor de la lista numbers ', max(numbers))
print('')
print('El menor de la lista numbers ', min(numbers))
print('')

print('++++++++++++++ Eliminar elementos de la lista numbers +++++++++++++++++++++')

del numbers[-1]

print('Nueva lista después de elminar el último elemento ', numbers)
print('')

del numbers[0:2]

print('Nueva lista después de elminar elementos 0 y 1 ', numbers)
print('')




