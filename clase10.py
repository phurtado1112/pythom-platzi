numbers = {1: 'uno', 2: 'dos', 3: 'tres'}
print(numbers)
print(numbers[2])
print('')

informacion = {'nombre':'Pablo', 'Apellido':'Hurtado', 'Altura':1.65, 'Edad':60}

print(informacion)
print('')

del informacion['Edad']

print(informacion)
print('')

print('+++++++++++ claves +++++++++++')

claves = informacion.keys()
print(claves)
print('')

print('+++++++++++ Valores +++++++++++')

valores = informacion.values()
print(valores)
print('')

print('+++++++++++ pares +++++++++++')

pares = informacion.items()
print(pares)
print('')

print('============================================')

contactos ={'Pablo': {'Apellido':'Hurtado', 'Altura':1.65, 'Edad':60 }, 'Martha':{'Apellido':'Díaz', 'Altura':1.60, 'Edad':45}}
print(contactos)
print('')
print(contactos['Pablo'])
print('')