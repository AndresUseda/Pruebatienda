from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/tienda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

# Importar los modelos

from models import Product

# Crear esquema de la base de datos

db.create_all()
db.session.commit()

# Rutas de Páginas

@app.route("/")
def get_home():
    return "Este es el home"

@app.route("/signup")
def sign_up():
    return "Este es la página de registro"

# Rutas de otras acciones
@app.route("/product", methods=["GET", "POST"])
def crud_product():
    if request.method == "GET":

        # Pedir un producto
        print("Llegó un GET")

        # Insertar producto
        name = "Jabon de cuerpo"
        brand = "Palmolive"
        presentation = "barra"
        category = "Aseo"
        price = 2500
        amount = 1
        due_date = datetime.datetime(int(2001), int(9), int(24))
        income_type = "proveedor"
        supplier = "Makro"
        location = "Estante 1"

        entry = Product(name,brand,presentation,category,price,amount,due_date,income_type,supplier,location)
        db.session.add(entry)
        db.session.commit()
        
        return "Esto fue un GET"

    elif request.method == "POST":

        # Registrar un producto
        request_data = request.form
        name = request_data["name"]
        brand = request_data["brand"]
        presentation = request_data["presentation"]
        category = request_data["category"]
        price = request_data["price"]

        print("Nombre:" + name)
        print("Marca:" + brand)
        print("Presentación:" + presentation)
        print("Categoria:" + category)
        print("Precio:" + price)

        # Insertar en la base de datos el producto

        return "Se registró el producto exitosamente"

# Actualizar productos
@app.route('/updateproduct')
def update_product():
    old_name = "Jabon de cuerpo"
    new_name = "Jabon de loza"
    old_product = Product.query.filter_by(name=old_name).first()
    old_product.name = new_name
    db.session.commit()
    return "Actualización exitosa"

# Consultar productos
@app.route('/getproduct')
def get_product():
    songs = Product.query.all()
    print(Product[0].category)
    return "Se trajo la lista de productos"

# Eliminar productos
@app.route('/deleteproduct')
def delete_product():
    product_name = "Jabon de cuerpo"
    product = Product.query.filter_by(name=product_name).first()
    db.session.delete(product)
    db.session.commit()
    return "Se borro el producto"