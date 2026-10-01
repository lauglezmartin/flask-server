from flask import Flask, render_template

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
@app.route("/catalogo/<int:id_producto>")
def catalogo(id_producto):
    productos =[
        {"id": 1, "nombre": "Teclado", "precio": 10.99, "disponible": True},
        {"id": 2, "nombre": "Monitor", "precio": 199.99, "disponible": False},
        {"id": 3, "nombre": "Ratón", "precio": 5.49, "disponible": True},
    ]
    return render_template("catalogo.html", nombre="algo", id_producto=id_producto, lista_productos=productos)

# Ruta 5: Devuelve un saludo personalizado con nombre y edad
@app.route("/saludo/<name>/<int:edad>")
def saludo_personalizado(name, edad):
    return f"""
        <h1>¡Hola {name}!</h1>
        <p>Tienes {edad} años.</p>
    """
render_template("index.html", nombre="Juan", edad=30)



if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
