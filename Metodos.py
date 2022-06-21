texto = "Este es el texto de Milton"
#resultado = texto.lower() #hace minusculas todo el texto
#resultado = texto.upper() #hace mayusculas todo el texto
#resultado = texto[2:10].lower() #definimos de que parametro a que parametro queremos y tambien esos parametros estaran en este caso en minuscula
#resultado = texto.split("t") #separa el texto en una lista #si agregamos una letra crea un criterio de separacion
#resultado = texto.find("texto")#busca un determinado caraccter
#resultado = texto.replace("Milton", "Todos") #remplaza el texto que tenemos, por otra palabra o texto, por lo que agregamos el parametro ("Palabra o string del texto", Nuevo String)
resultado = texto.replace("e", "x") #remplazar todo el texto e a cambio de una x
print(resultado)

#a = "Aprender"
#b = "Python"
#c = "es"
#d = "genial"
#e = " ".join([a, b, c, d]) #join sirve para agregar un texto dependiendo los parametros que encontramos en una lista, ejemplo agregamos un espacio entre cada uno de ellos
#print(e)