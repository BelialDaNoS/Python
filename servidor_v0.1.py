from flask import Flask

app = Flask("mi_servidor")

@app.route("/")
def home():
    return "Este es mi primer servidor! Bienvenidos"

@app.route("/otra-ruta")
def otra_ruta():
    return "Otra Ruta"



app.run(debug=True, port=8182)