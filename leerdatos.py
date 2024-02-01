import sqlite3

def leer_datos():
  conn = sqlite3.connect("censo.db")
  cursor = conn.cursor()

  cursor.execute('SELECT * FROM censo LIMIT 10:')

#Obtener y mostrar los datos

rows = cursor.fetchall()
for 