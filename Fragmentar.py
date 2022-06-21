texto = "ABCDEFGHIJKLM"
#fragmento = texto[2]
#fragmento = texto[2:5] #el punto representa de que valor a que valor queremos obtener los datos
#fragmento = texto[2:10:2]#Fragmento inicial:fragmento final: cada cuantos caracteres se tomaran en este caso de 2 en 2
fragmento = texto[::-2] #al dejar los :: en blanco nos permite tomar todos, pero si agregamos un numero despues del ultimo : nos permite ir de 2 en 2 en este caso, negativos van de derecha a izquierda
print(fragmento)
