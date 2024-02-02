import sqlite3

def leerdatos():
  conn = sqlite3.connect("pv_model.db")
  cursor = conn.cursor()

  cursor.execute('SELECT * FROM pycharm LIMIT 10;')

  # Obtener y mostrar los datos
  rows = cursor.fetchall()
  for row in rows:
    print(row)  # Aquí puedes ajustar la forma en que se muestran los datos

  # Cerrar la conexión a la base de datos
  conn.close()

if __name__ == '__main__':
    leerdatos()