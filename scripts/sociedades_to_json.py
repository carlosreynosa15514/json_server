import sqlite3
import json
from numpy import append

# Conexion a la base de datos
conn = sqlite3.connect("C:/Users/cmoreno/OneDrive/Cursos Practicos/Proyecto Python/Catalogos/catalogos.db")

# Crear cursor para gestionar los queries de sql
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM sociedades")
resultado = cursor.fetchall()

# Se crea la lista vacia para poner los diccionarios
lista = []

# Se itera sobre el resultado del query de sql
for item in resultado:
    # se crea cada diccionario para hacer la lista de diccionarios para convertir a json
    dict_item = {'soc':item[0], 'sociedad':item[1], 'pais':item[2], 'moneda':item[3]}
    lista.append(dict_item)

# Se graba la lista de duccionarios en formato json
with open('db1.jason', 'w') as f:
    json.dump(lista,f)

    
    


