from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)

# -----------------------
# MODELOS
# -----------------------
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    usuario = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()

# -----------------------
# REGISTRO
# -----------------------
@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()

    username = datos.get('usuario')
    password = datos.get('password')

    if not username or not password:
        return jsonify({"mensaje": "Faltan datos"}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"mensaje": "Usuario ya existe"}), 400

    user = Usuario(
        username=username,
        password_hash=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"mensaje": "Usuario creado"})

# -----------------------
# LOGIN
# -----------------------
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()

    username = datos.get('usuario')
    password = datos.get('password')

    user = Usuario.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):
        session['usuario'] = username
        return jsonify({"mensaje": "Login exitoso"})

    return jsonify({"mensaje": "Credenciales incorrectas"}), 401

# -----------------------
# LOGOUT
# -----------------------
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario', None)
    return jsonify({"mensaje": "Sesión cerrada"})

# -----------------------
# GET /tareas (HTML - CONSIGNA)
# -----------------------
@app.route('/tareas', methods=['GET'])
def tareas():

    usuario = session.get('usuario')

    if not usuario:
        return """
    <h2>No autorizado</h2>
    <p>Debes iniciar sesión</p>
    """, 401

    tareas = Tarea.query.filter_by(usuario=usuario).all()

    lista = "\n".join([
    f"<li style='margin:10px 0;'>ID: {t.id} - {t.titulo}</li>"
    for t in tareas
])
    return f"""
<html>
    <body style="font-family:Arial; text-align:center; margin-top:60px;">
        <h1>Bienvenido {usuario}</h1>
        <p>Estas son tus tareas:</p>

        <ul style="list-style:none; padding:0;">
            {lista}
        </ul>
    </body>
</html>
"""

# -----------------------
# CREAR TAREA
# -----------------------
@app.route('/tareas', methods=['POST'])
def crear_tarea():

    usuario = session.get('usuario')

    if not usuario:
        return jsonify({"mensaje": "No autorizado"}), 401

    datos = request.get_json()
    titulo = datos.get('titulo')

    if not titulo:
        return jsonify({"mensaje": "Falta título"}), 400

    tarea = Tarea(titulo=titulo, usuario=usuario)

    db.session.add(tarea)
    db.session.commit()

    return jsonify({"mensaje": "Tarea creada"})

# -----------------------
# BORRAR TAREA
# -----------------------
@app.route('/tareas/<int:id>', methods=['DELETE'])
def borrar_tarea(id):

    usuario = session.get('usuario')

    if not usuario:
        return jsonify({"mensaje": "No autorizado"}), 401

    tarea = Tarea.query.filter_by(id=id, usuario=usuario).first()

    if not tarea:
        return jsonify({"mensaje": "No encontrada"}), 404

    db.session.delete(tarea)
    db.session.commit()

    return jsonify({"mensaje": "Tarea eliminada"})

# -----------------------
# MAIN
# -----------------------
if __name__ == '__main__':
    app.run(debug=True)