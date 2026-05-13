# 🦷 Denova

**Denova** es una plataforma web desarrollada con **Flask**, diseñada para la gestión inteligente de clínicas dentales.

Integra una arquitectura híbrida utilizando:

- **MongoDB Atlas** → almacenamiento NoSQL
- **SQLite** → almacenamiento relacional
- **JWT Authentication** → autenticación segura
- **RBAC (Role Based Access Control)** → control de acceso por roles
- **Bootstrap 5** → interfaz moderna y responsive

---

# 📌 Características principales

## 🔐 Sistema de autenticación
- Registro de usuarios
- Inicio de sesión seguro
- Contraseñas cifradas
- Tokens JWT
- Protección de rutas

---

## 👥 Gestión de roles
El sistema distingue entre:

### Administrador
Puede:

- Acceder al panel administrativo
- Gestionar usuarios
- Consultar estadísticas
- Administrar leads
- Revisar actividad del sistema

### Doctor
Puede:

- Acceder a funciones limitadas
- Consultar información asignada
- Interactuar con SYRA

---

## 🤖 Chatbot SYRA
Asistente inteligente capaz de:

- Responder consultas
- Registrar interacciones
- Guardar historial en SQLite
- Simular atención automatizada

---

## 📊 Dashboard administrativo
Panel visual con:

- Métricas
- Actividad reciente
- Estadísticas de usuarios
- Gestión general del sistema

---

## 🗄️ Base de datos híbrida

### MongoDB Atlas
Almacena:

- Usuarios
- Leads
- Asesorías

### SQLite
Almacena:

- Logs de conversaciones con SYRA
- Historial de interacciones

---

# 🧱 Tecnologías utilizadas

- Python 3.11+
- Flask
- Flask-JWT-Extended
- MongoDB Atlas
- PyMongo
- SQLite3
- Bootstrap 5
- HTML5
- CSS3
- JavaScript

---

# 📂 Estructura del proyecto

```bash
Denova/
│
├── app.py
├── config.py
├── README.md
│
├── routes/
│   └── auth_routes.py
│
├── database/
│   └── sqlite_db.py
│
├── utils/
│   └── decorators.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   └── admin.html
│
└── instance/
    └── app.db
```

---

# ⬇️ Cómo descargar el proyecto

## Opción 1: Descargar ZIP

1. Ir al repositorio
2. Clic en **Code**
3. Seleccionar **Download ZIP**
4. Extraer archivos

---

## Opción 2: Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar al proyecto:

```bash
cd Denova
```

---

# ⚙️ Instalación

Instalar dependencias:

```bash
pip install flask
pip install pymongo
pip install flask-jwt-extended
pip install werkzeug
```

O:

```bash
pip install -r requirements.txt
```

---

# 🛠 Configuración

Editar:

```python
config.py
```

Configurar:

```python
MONGO_URI
SECRET_KEY
JWT_SECRET_KEY
```

Ejemplo:

```python
MONGO_URI = "tu_uri_mongodb"
SECRET_KEY = "clave_secreta"
JWT_SECRET_KEY = "jwt_clave"
```

---

# ▶️ Cómo ejecutar el proyecto

Desde terminal:

```bash
python app.py
```

Si todo funciona aparecerá:

```bash
Running on http://127.0.0.1:5000
```

Abrir navegador:

```bash
http://127.0.0.1:5000
```

---

# 🔑 Registro de usuario

Endpoint:

```bash
/auth/register
```

Ejemplo JSON:

```json
{
  "nombre": "Admin",
  "email": "admin@test.com",
  "password": "123456",
  "role": "admin"
}
```

---

# 🔓 Inicio de sesión

Ruta:

```bash
/login
```

Credenciales ejemplo:

```txt
admin@test.com
123456
```

---

# 📡 Endpoints disponibles

## Usuarios

```bash
/api/usuarios
```

---

## Leads

```bash
/api/leads
```

---

## Asesorías

```bash
/api/asesorias
```

---

## Chatbot SYRA

```bash
/api/syra
```

---

## Estadísticas híbridas

```bash
/api/usuario/<id>/estadisticas
```

---

# 🔒 Seguridad implementada

- JWT Authentication
- Contraseñas cifradas
- Validación de roles
- Protección de endpoints
- Control de acceso por permisos

---

# 🚀 Mejoras futuras

- Dashboard doctor
- CRUD visual completo
- Reportes exportables
- IA avanzada para SYRA
- Despliegue en producción
- Integración con WhatsApp API

---

# 👩‍💻 Autora

**Mariangel**

Proyecto académico y profesional desarrollado como plataforma inteligente de gestión dental.