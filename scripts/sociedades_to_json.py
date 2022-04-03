import sqlite3
import json

from numpy import append

# Conexion
conn = sqlite3.connect("C:/Users/cmoreno/OneDrive/Cursos Practicos/Proyecto Python/Catalogos/catalogos.db")

# Crear cursor
cursor = conn.cursor()

lista  = []
dicc = {}
keys = ['soc', 'socedad', 'pais', 'moneda']
cursor.execute(f"SELECT * FROM sociedades")
resultado = cursor.fetchall()

for item in resultado:
    dict_item = {'soc':item[0], 'sociedad':item[1], 'pais':item[2], 'moneda':item[3]}
    lista.append(dict_item)

with open('db1.jason', 'w') as f:
    json.dump(lista,f)

    
    


