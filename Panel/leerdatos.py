import sqlite3

def leer_datos():
  conn = sqlite3.connect("censo.db")
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM censo LIMIT 10;')

  #obtener y mostrar los datos
  rows = cursor.fetchall()
  for row in rows:
    print(row)

  conn.close()

if __name__ == '__main__':
  leer_datos()
