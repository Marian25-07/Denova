from flask import Flask, jsonify, request

app = Flask(__name__)

# =========================
# BASE DE DATOS (SIMULADA)
# =========================
usuarios = []
leads = []
asesorias = []

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
            "/api/syra"
        ]
    })

# =========================
# USUARIOS
# =========================

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    return respuesta_ok(usuarios)

@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    if not data or 'nombre' not in data:
        return respuesta_error("El nombre es obligatorio")

    nuevo = {
        "id": len(usuarios) + 1,
        "nombre": data["nombre"],
        "email": data.get("email"),
        "telefono": data.get("telefono"),
        "tipo_usuario": "doctor"
    }

    usuarios.append(nuevo)
    return respuesta_ok(nuevo, "Usuario creado")

# =========================
# LEADS
# =========================

@app.route('/api/leads', methods=['GET'])
def get_leads():
    return respuesta_ok(leads)

@app.route('/api/leads', methods=['POST'])
def crear_lead():
    data = request.get_json()

    if not data or 'id_usuario' not in data:
        return respuesta_error("Falta id_usuario")

    nuevo = {
        "id": len(leads) + 1,
        "id_usuario": data["id_usuario"],
        "estado": "nuevo",
        "origen": data.get("origen", "web")
    }

    leads.append(nuevo)
    return respuesta_ok(nuevo, "Lead creado")

# =========================
# ASESORÍAS
# =========================

@app.route('/api/asesorias', methods=['GET'])
def get_asesorias():
    return respuesta_ok(asesorias)

@app.route('/api/asesorias', methods=['POST'])
def crear_asesoria():
    data = request.get_json()

    if not data or 'id_usuario' not in data or 'fecha' not in data:
        return respuesta_error("Datos incompletos")

    nueva = {
        "id": len(asesorias) + 1,
        "id_usuario": data["id_usuario"],
        "fecha": data["fecha"],
        "estado": "agendada"
    }

    asesorias.append(nueva)
    return respuesta_ok(nueva, "Asesoría agendada")

# =========================
# SYRA (IA SIMULADA)
# =========================

@app.route('/api/syra', methods=['POST'])
def syra():
    data = request.get_json()

    mensaje = data.get("mensaje", "").lower()

    if "precio" in mensaje:
        respuesta = "Nuestros servicios se adaptan a tu clínica. Agenda una asesoría 😉"
    elif "hola" in mensaje:
        respuesta = "Hola 👋 soy SYRA, te ayudo a crecer tu clínica"
    elif "info" in mensaje:
        respuesta = "Denova transforma clínicas con alineadores 🚀"
    else:
        respuesta = "Cuéntame más y te ayudo 😉"

    return respuesta_ok({
        "mensaje_usuario": mensaje,
        "respuesta": respuesta
    }, "Respuesta generada")

# =========================
# EJECUCIÓN
# =========================
if __name__ == '__main__':
    app.run(debug=True)