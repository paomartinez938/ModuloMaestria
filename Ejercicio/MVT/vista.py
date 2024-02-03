from modelo import obtener_libros

def mostrar_libros():
  libros = obtener_libros()
  for libro in libros:
    print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}")