from flask import Flask, jsonify, request
from pymongo import MongoClient
import sqlite3
app = Flask(__name__)

# =========================
# CONEXION MONGO (NoSQL)
# =========================

client = MongoClient('mongodb+srv://Kamilo:1234KL@denova.kdqkau6.mongodb.net/?appName=Denova')
db = client['bd1']
collection_usuarios = db['usuarios']
collection_leads = db['leads']
collection_asesorias = db['asesorias']

# =========================
# CONEXION SQLITE (SQL)
# =========================

def get_db():
    conn = sqlite3.connect('denova.db')
    conn.row_factory = sqlite3.Row
    return conn

# Crear tabla de logs si no existe
def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS logs_syra (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                mensaje TEXT,
                respuesta TEXT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

init_db()

# =========================
# BASE DE DATOS (SIMULADA) - AHORA USANDO MONGODB
# =========================
# usuarios = []  # Removido, ahora usa MongoDB
# leads = []
# asesorias = []

# =========================
# UTILIDADES
# =========================
def respuesta_ok(data, mensaje="ok"):
    return jsonify({
        "status": "success",
        "mensaje": mensaje,
        "data": data
    }), 200

def respuesta_error(mensaje="error"):
    return jsonify({
        "status": "error",
        "mensaje": mensaje
    }), 400

# =========================
# RUTA PRINCIPAL
# =========================
@app.route('/')
def inicio():
    return jsonify({
        "api": "Denova API 🚀",
        "version": "1.0",
        "endpoints": [
            "/api/usuarios",
            "/api/leads",
            "/api/asesorias",
            "/api/syra",
            "/api/usuario/<id>/estadisticas"
        ]
    })

# =========================
# USUARIOS
# =========================

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = list(collection_usuarios.find({}, {'_id': 0}))
    return respuesta_ok(usuarios)

@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    if not data or 'nombre' not in data:
        return respuesta_error("El nombre es obligatorio")

    nuevo = {
        "id": len(list(collection_usuarios.find())) + 1,  # Contar documentos para id
        "nombre": data["nombre"],
        "email": data.get("email"),
        "telefono": data.get("telefono"),
        "tipo_usuario": "doctor"
    }

    collection_usuarios.insert_one(nuevo)
    return respuesta_ok(nuevo, "Usuario creado")

# =========================
# LEADS
# =========================

@app.route('/api/leads', methods=['GET'])
def get_leads():
    leads = list(collection_leads.find({}, {'_id': 0}))
    return respuesta_ok(leads)

@app.route('/api/leads', methods=['POST'])
def crear_lead():
    data = request.get_json()

    if not data or 'id_usuario' not in data:
        return respuesta_error("Falta id_usuario")

    nuevo = {
        "id": len(list(collection_leads.find())) + 1,
        "id_usuario": data["id_usuario"],
        "estado": "nuevo",
        "origen": data.get("origen", "web")
    }

    collection_leads.insert_one(nuevo)
    return respuesta_ok(nuevo, "Lead creado")

# =========================
# ASESORÍAS
# =========================

@app.route('/api/asesorias', methods=['GET'])
def get_asesorias():
    asesorias = list(collection_asesorias.find({}, {'_id': 0}))
    return respuesta_ok(asesorias)

@app.route('/api/asesorias', methods=['POST'])
def crear_asesoria():
    data = request.get_json()

    if not data or 'id_usuario' not in data or 'fecha' not in data:
        return respuesta_error("Datos incompletos")

    nueva = {
        "id": len(list(collection_asesorias.find())) + 1,
        "id_usuario": data["id_usuario"],
        "fecha": data["fecha"],
        "estado": "agendada"
    }

    collection_asesorias.insert_one(nueva)
    return respuesta_ok(nueva, "Asesoría agendada")

# =========================
# ENDPOINT HÍBRIDO (SQL + NoSQL)
# =========================

@app.route('/api/usuario/<int:id_usuario>/estadisticas', methods=['GET'])
def estadisticas_usuario(id_usuario):
    # Datos de MongoDB (NoSQL)
    usuario = collection_usuarios.find_one({'id': id_usuario}, {'_id': 0})
    if not usuario:
        return respuesta_error("Usuario no encontrado")

    leads_count = collection_leads.count_documents({'id_usuario': id_usuario})
    asesorias_count = collection_asesorias.count_documents({'id_usuario': id_usuario})

    # Datos de SQLite (SQL)
    with get_db() as conn:
        logs = conn.execute('SELECT COUNT(*) as total_logs, MAX(fecha) as ultima_interaccion FROM logs_syra WHERE id_usuario = ?',
                           (id_usuario,)).fetchone()

    return respuesta_ok({
        "usuario": usuario,
        "estadisticas": {
            "leads_generados": leads_count,
            "asesorias_agendadas": asesorias_count,
            "interacciones_syra": logs['total_logs'],
            "ultima_interaccion_syra": logs['ultima_interaccion']
        }
    }, "Estadísticas combinadas SQL + NoSQL")

@app.route('/api/syra', methods=['POST'])
def syra():
    data = request.get_json()

    mensaje = data.get("mensaje", "").lower()
    id_usuario = data.get("id_usuario")  # Nuevo campo opcional

    if "precio" in mensaje:
        respuesta = "Nuestros servicios se adaptan a tu clínica. Agenda una asesoría 😉"
    elif "hola" in mensaje:
        respuesta = "Hola 👋 soy SYRA, te ayudo a crecer tu clínica"
    elif "info" in mensaje:
        respuesta = "Denova transforma clínicas con alineadores 🚀"
    else:
        respuesta = "Cuéntame más y te ayudo 😉"

    # Guardar log en SQL
    if id_usuario:
        with get_db() as conn:
            conn.execute('INSERT INTO logs_syra (id_usuario, mensaje, respuesta) VALUES (?, ?, ?)',
                        (id_usuario, mensaje, respuesta))
            conn.commit()

    return respuesta_ok({
        "mensaje_usuario": mensaje,
        "respuesta": respuesta
    }, "Respuesta generada")

# =========================
# EJECUCIÓN
# =========================
if __name__ == '__main__':
    app.run(debug=True)