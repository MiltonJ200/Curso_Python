#mi_tuple = (1,2,(10,20),4)

#mi_tuple= list(mi_tuple) #podemos tranformar un tuple a lista sin problemas
#mi_tuple[0] = 5 #son inmutables no se puede modificar el contenido de un tuple


#print(mi_tuple[2][0]) #podemos buscar como en las listas y diccionarios
#mi_tuple = tuple(mi_tuple)

#t = (1,2,3)

#x,y,z = t

#print(x, y, z)

t = (1,2,3,1)


print(t.count(1)) #metodo count cuenta los valores que se encuentran dentro del tuple

print(t.index(2)) #cual es el valor sobre en que indice se encuentra

#Ejercicios

#Ejercicio 1
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(mi_tupla.count(2))

#ejercicio 2
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

mi_lista = list(mi_tupla)

#ejercicio 3
mi_tupla = (1, 2, 3, 4)

a = mi_tupla[0]
b = mi_tupla[1]
c = mi_tupla[2]
d = mi_tupla[3]