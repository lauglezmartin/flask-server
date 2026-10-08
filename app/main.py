from data.productos import productos
from flask import Flask, render_template, request

# Inicializamos la aplicación
app = Flask(__name__)


# Ruta 0: Devuelve un saludo simple
@app.route("/saludo/")
def saludo():
    return """
        <h1>¡Hola desde Flask en Docker!!!!</h1>
        <p>Este es tu primer servidor Python funcionando.</p>
    """


# Ruta 1: Devuelve un HTML renderizado con Jinja2
@app.route("/")
def home():
    return render_template("index.html")


# Ruta 2: Devuelve un saludo
@app.route("/saludo/<name>")
def hello(name):
    return f"""
        <h1>¡Bienvenido a Flask en Docker!, {name}</h1>
    """


# Ruta 3: Devuelve la multiplicación de dos números
@app.route("/multiplicar/<int:numero1>/<int:numero2>")
def multiplicar(numero1, numero2):
    return (
        f"<h1>Multiplicar {numero1} x {numero2} y da resultado {numero1 * numero2}</h1>"
    )


# Ruta 4: Devuelve un HTML renderizado con Jinja2
@app.route("/catalogo/")
def catalogo():
    return render_template(
        "catalogo.html",
        nombre="algo",
        lista_productos=productos,
    )


@app.route("/catalogo/<int:idProducto>")
def producto(idProducto):
    return render_template(
        "producto.html", idProducto=idProducto, producto=productos[idProducto])  

# Ruta 5: Devuelve un saludo personalizado con nombre y edad
@app.route("/saludo/<name>/<int:edad>")
def saludo_personalizado(name, edad):
    return render_template("saludo.html", nombre=name, edad=edad)


@app.route("/contacto", methods=["GET"])
def contacto():
    return render_template("contacto.html")


@app.route("/contacto", methods=["POST"])
def contacto_post():
    nombre = request.form.get("nombre")
    mensaje = request.form.get("mensaje")
    return render_template("contactos-datos.html", nombre=nombre, mensaje=mensaje)

@app.route("/filtrar")
def filtrar():
    return render_template("filtrar.html")

@app.route("/filtrar-data", methods=["GET"])
def filtrar_data():
    precio_min = request.args.get("precio_min", type=float)
    precio_max = request.args.get("precio_max", type=float)
    print(f"Precio mínimo: {precio_min}, Precio máximo: {precio_max}")
    productos_filtrados =[
        producto for producto in productos if producto["precio"] >= precio_min and producto["precio"] <= precio_max]
    # return render_template("filtrar-data.html")
    return render_template("catalogo.html", nombre = "Filtrado", lista_productos=productos_filtrados)



if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)


