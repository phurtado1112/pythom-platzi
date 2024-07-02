numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
  print('i es igual a: ',i)

print('')

for i in range(10):
  print('i es igual a en el rango de 0 al 9: ', i)

print('')

for i in range(1,11):
  print('i es igual a en el rango de 1 al 10: ', i)

print('')

print('++++++++++++++++++ For +++++++++++++++++++')

fruits = ['Manzana', 'Pera', 'Uva', 'Naranja', 'Tomate']

for fruit in fruits:
  print(fruit)
  if fruit == 'Naranja':
    print('Naranja encontrado')

print('')

print('++++++++++++++++++ While + Break con valor de 3 +++++++++++++++++++')

x = 0
while x < 5:
  if x == 3:
    break
  print('El valor de x = ', x)
  x += 1

print('')

print('++++++++++++++++++ While + Continue +++++++++++++++++++')

other_numbres = range(1, 10)

for i in other_numbres:
  if i == 3:
    continue
  print('El valor de i = ', i)