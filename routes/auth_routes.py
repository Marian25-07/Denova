from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client['bd1']
users_collection = db['usuarios']

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No se enviaron datos"}), 400

    nombre = data.get("nombre")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not all([nombre, email, password, role]):
        return jsonify({
            "message": "Faltan campos requeridos: nombre, email, password, role"
        }), 400

    if role not in ["admin", "doctor"]:
        return jsonify({
            "message": "Rol inválido. Debe ser admin o doctor"
        }), 400

    if users_collection.find_one({"email": email}):
        return jsonify({
            "message": "Ya existe un usuario con ese email"
        }), 409

    hashed_password = generate_password_hash(password)

    nuevo_usuario = {
        "nombre": nombre,
        "email": email,
        "password": hashed_password,
        "role": role
    }

    users_collection.insert_one(nuevo_usuario)

    return jsonify({
        "message": "Usuario registrado correctamente"
    }), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No se enviaron datos"}), 400

    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return jsonify({
            "message": "Faltan email y password"
        }), 400

    user = users_collection.find_one({"email": email})

    if not user:
        return jsonify({
            "message": "Credenciales inválidas"
        }), 401

    if not check_password_hash(user["password"], password):
        return jsonify({
            "message": "Credenciales inválidas"
        }), 401

    access_token = create_access_token(identity={
        "email": user["email"],
        "role": user["role"],
        "nombre": user["nombre"]
    })

    return jsonify({
        "message": "Login exitoso",
        "access_token": access_token,
        "user": {
            "nombre": user["nombre"],
            "email": user["email"],
            "role": user["role"]
        }
    }), 200