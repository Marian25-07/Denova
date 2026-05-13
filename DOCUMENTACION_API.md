# 📡 Documentación Técnica de la API — Denova

## 📌 Descripción General

La API de **Denova** fue desarrollada utilizando **Flask** y permite la gestión híbrida de información mediante:

- MongoDB Atlas (NoSQL)
- SQLite (SQL)

La API proporciona funcionalidades para:

- Gestión de usuarios
- Gestión de leads
- Gestión de asesorías
- Chatbot inteligente SYRA
- Autenticación JWT
- Control de acceso por roles

---

# 🏗 Arquitectura

## Backend

- Flask
- Flask-JWT-Extended
- PyMongo
- SQLite3

---

## Bases de datos

### MongoDB Atlas

Colecciones utilizadas:

- usuarios
- leads
- asesorias
- users

---

### SQLite

Tabla utilizada:

```sql
logs_syra
```

Campos:

| Campo | Tipo |
|---|---|
| id | INTEGER |
| id_usuario | TEXT |
| mensaje | TEXT |
| respuesta | TEXT |
| fecha | TEXT |

---

# 🔐 Sistema de autenticación

La API utiliza:

- JWT Authentication
- Hash de contraseñas
- Roles de usuario

Roles disponibles:

- admin
- doctor

---

# 🌐 URL base

```bash
http://127.0.0.1:5000
```

---

# 📡 Endpoints

---

# 👤 Usuarios

---

## Obtener usuarios

### Endpoint

```http
GET /api/usuarios
```

### Descripción

Obtiene todos los usuarios registrados.

---

### Respuesta exitosa

```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "nombre": "Juan"
    }
  ]
}
```

---

## Crear usuario

### Endpoint

```http
POST /api/usuarios
```

---

### Body JSON

```json
{
  "nombre": "Juan",
  "email": "juan@test.com",
  "telefono": "3000000000"
}
```

---

### Respuesta exitosa

```json
{
  "status": "success",
  "mensaje": "Usuario creado"
}
```

---

# 📈 Leads

---

## Obtener leads

### Endpoint

```http
GET /api/leads
```

---

## Crear lead

### Endpoint

```http
POST /api/leads
```

---

### Body JSON

```json
{
  "id_usuario": 1,
  "origen": "web"
}
```

---

### Respuesta

```json
{
  "status": "success",
  "mensaje": "Lead creado"
}
```

---

# 📅 Asesorías

---

## Obtener asesorías

### Endpoint

```http
GET /api/asesorias
```

---

## Crear asesoría

### Endpoint

```http
POST /api/asesorias
```

---

### Body JSON

```json
{
  "id_usuario": 1,
  "fecha": "2026-05-12"
}
```

---

### Respuesta

```json
{
  "status": "success",
  "mensaje": "Asesoría agendada"
}
```

---

# 🤖 Chatbot SYRA

---

## Generar respuesta automática

### Endpoint

```http
POST /api/syra
```

---

### Body JSON

```json
{
  "id_usuario": 1,
  "mensaje": "hola"
}
```

---

### Respuesta

```json
{
  "status": "success",
  "data": {
    "respuesta": "Hola 👋 soy SYRA"
  }
}
```

---

# 📊 Estadísticas híbridas

Este endpoint combina información de:

- MongoDB
- SQLite

---

## Obtener estadísticas de usuario

### Endpoint

```http
GET /api/usuario/<id>/estadisticas
```

---

### Ejemplo

```http
GET /api/usuario/1/estadisticas
```

---

### Respuesta

```json
{
  "status": "success",
  "data": {
    "usuario": {},
    "estadisticas": {
      "leads_generados": 5,
      "asesorias_agendadas": 2,
      "interacciones_syra": 10
    }
  }
}
```

---

# 🔐 Autenticación

---

## Registro de usuario

### Endpoint

```http
POST /auth/register
```

---

### Body JSON

```json
{
  "nombre": "Admin",
  "email": "admin@test.com",
  "password": "123456",
  "role": "admin"
}
```

---

### Respuesta

```json
{
  "message": "User registered successfully"
}
```

---

## Inicio de sesión

### Endpoint

```http
POST /auth/login
```

---

### Body JSON

```json
{
  "email": "admin@test.com",
  "password": "123456"
}
```

---

### Respuesta

```json
{
  "access_token": "jwt_token"
}
```

---

# 🔒 Seguridad implementada

## JWT

Los endpoints protegidos requieren token JWT.

---

## Roles

El sistema valida:

- admin
- doctor

---

## Contraseñas

Las contraseñas son almacenadas usando hash seguro.

---

# ⚠️ Códigos de respuesta

| Código | Significado |
|---|---|
| 200 | OK |
| 201 | Creado |
| 400 | Error de solicitud |
| 401 | No autorizado |
| 403 | Acceso denegado |
| 404 | No encontrado |
| 500 | Error interno |

---

# 🧪 Herramientas recomendadas para pruebas

- Postman
- Thunder Client
- Insomnia

---

# 🚀 Futuras mejoras

- Swagger/OpenAPI
- Validación avanzada
- Refresh tokens
- Rate limiting
- Logs avanzados
- Integración IA real para SYRA

---

# 👩‍💻 Autores

Kerly Mariangel Alvarado Arias
Juan Kamilo Chacon Arias

Proyecto académico y profesional desarrollado para gestión inteligente de clínicas dentales.