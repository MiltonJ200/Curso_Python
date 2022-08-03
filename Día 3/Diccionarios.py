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

#ejercicios

#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista

#ejercicio 1
mi_dic = {'nombre':'Karen', 'apellido':'Jurgens', 'edad':35, 'ocupacion': 'Periodista'}

#ejercicio 2
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}

print(mi_dict["puntos"]["points2"][1])

#ejercicio 3
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"