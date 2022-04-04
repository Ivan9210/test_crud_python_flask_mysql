from flask import Flask, render_template, request, redirect
import controlador_libros

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route("/agregar_libro")
def formulario_agregar_libro():
    return render_template("agregar_libro.html")


@app.route("/guardar_libro", methods=["POST"])
def guardar_libro():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_libros.insertar_libro(nombre, descripcion, precio)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/libros")

@app.route("/")
@app.route("/libros")
def libros():
    libros = controlador_libros.obtener_libros()
    return render_template("libros.html", libros=libros)


@app.route("/eliminar_libro", methods=["POST"])
def eliminar_libro():
    controlador_libros.eliminar_libro(request.form["id"])
    return redirect("/libros")


@app.route("/formulario_editar_libro/<int:id>")
def editar_libro(id):
    # Obtener el libro por ID
    libro = controlador_libros.obtener_libro_por_lib_id(id)
    return render_template("editar_libro.html", libro=libro)


@app.route("/actualizar_libro", methods=["POST"])
def actualizar_libro():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_libros.actualizar_libro(nombre, descripcion, precio, id)
    return redirect("/libros")


# Datos para iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)