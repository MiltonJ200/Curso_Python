#diccionario = {'c1':'valor1', 'c2':'valor2'}
#print(diccionario)

#resultado = diccionario['c2']
#print(resultado)

#cliente = {'nombre':'Juan', 'apellido':'Fuentes', 'peso': 88, 'talla':1.76}
#consulta = (cliente['talla'])
#print(consulta)

#dic = {'c1':55,'c2':[18,28,38],'c3':{'s1':100,'s2':200}}

#print(dic['c2'][2])
#print(dic['c3']["s1"])

#dic = {'c1':['a', 'b', 'c'], 'c2':['d','e','f']}
#resultado = dic['c2'][1]
#print(dic['c2'][1].upper())

dic = {1:'a',2:'b'}
print(dic)

dic[3] = 'c' #agrega valores al diccionario
print(dic)

dic[2] = 'B' #sobrescribe en el valor seleccionado

print(dic)

print(dic.keys())#para saber las claves
print(dic.values())#para saber los valores de las claves
print(dic.items())