from modelo import obtener_datos
#from template import renderizar_template

def renderizar_template(libros):
  #simular renderizar template
  html="<h1>lista de libros</h1>"
  for libro in libros:
    html += f"<p>ID: {libro['id']} Título: {libro['titulo']} Autor: {libro['autor']}</p>"
  return html

#Integrar la vista y el template

def mostrar_libros_con_template():
  libros = obtener_datos()
  html = renderizar_template(libros)
  print(html)

mostrar_libros_con_template()