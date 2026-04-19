Denova API

API REST desarrollada con Flask para la gestión de usuarios, leads, asesorías y automatización básica con SYRA.
Forma parte de la solución Denova, una plataforma orientada a la captación, seguimiento y conversión de leads para clínicas odontológicas.

📖 Descripción

Denova es una solución tecnológica que integra automatización e inteligencia artificial para optimizar procesos comerciales en clínicas dentales.

Esta API permite gestionar la lógica principal del sistema, incluyendo:

Registro de usuarios
Gestión de leads
Agendamiento de asesorías
Automatización básica de interacción (SYRA)

El proyecto está diseñado como una base inicial (MVP), con enfoque en evolución hacia una arquitectura más robusta que incluya integración con bases de datos SQL y NoSQL.

🧠 Enfoque Tecnológico

Actualmente el proyecto funciona con una arquitectura híbrida:

- **MongoDB Atlas**: Base de datos NoSQL para usuarios, leads y asesorías
- **SQLite**: Base de datos SQL para logs de interacciones SYRA
- **Flask**: Framework web para la API REST
- **Pymongo**: Driver para MongoDB

⚙️ Funcionalidades
- ✅ CRUD de usuarios (MongoDB)
- ✅ Gestión de leads (MongoDB)
- ✅ Registro de asesorías (MongoDB)
- ✅ Simulación de interacción con SYRA (SQLite logs)
- ✅ Endpoints REST para integración con frontend
- ✅ **Endpoint híbrido SQL + NoSQL** para estadísticas de usuario

## 📊 Evidencias de Ejecución

### Conexión a MongoDB Atlas
```bash
✅ Conexión exitosa a MongoDB Atlas
Bases de datos: ['bd1', 'sample_mflix', 'admin', 'local']
```

### Endpoint Híbrido (SQL + NoSQL)
```json
{
  "data": {
    "usuario": {
      "id": 1,
      "nombre": "Dr. Ana López",
      "email": "ana.lopez@clinica.com"
    },
    "estadisticas": {
      "leads_generados": 2,
      "asesorias_agendadas": 1,
      "interacciones_syra": 0,
      "ultima_interaccion_syra": null
    }
  },
  "mensaje": "Estadísticas combinadas SQL + NoSQL"
}
```

📦 Requisitos

Antes de empezar, se necesita tener instalado:

Python 3.8 o superior
Git
Cuenta en MongoDB Atlas (para la base de datos)

🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/denova-api.git
   cd denova-api
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
   > **Nota**: El entorno virtual (`venv/`) no se incluye en el repositorio porque contiene dependencias específicas del sistema. Se recrea fácilmente con `requirements.txt`.

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura MongoDB Atlas:
   - Crea un cluster en MongoDB Atlas
   - Obtén tu connection string
   - Actualiza la variable `MONGO_URI` en `app.py` (o usa variables de entorno)

5. Ejecuta la aplicación:
   ```bash
   python src/app.py
   ```

La API estará disponible en `http://127.0.0.1:5000/`

📡 Endpoints

### Usuarios
- `GET /api/usuarios` - Lista todos los usuarios
- `POST /api/usuarios` - Crea un nuevo usuario
  ```json
  {
    "nombre": "Dr. Juan Pérez",
    "email": "juan.perez@clinica.com",
    "telefono": "555-0123"
  }
  ```

### Leads
- `GET /api/leads` - Lista todos los leads
- `POST /api/leads` - Crea un nuevo lead
  ```json
  {
    "id_usuario": 1,
    "origen": "web"
  }
  ```

### Asesorías
- `GET /api/asesorias` - Lista todas las asesorías
- `POST /api/asesorias` - Crea una nueva asesoría
  ```json
  {
    "id_usuario": 1,
    "fecha": "2024-01-20"
  }
  ```

### SYRA (IA)
- `POST /api/syra` - Interacción con el asistente virtual
  ```json
  {
    "mensaje": "Hola, quiero información sobre precios",
    "id_usuario": 1
  }
  ```

### Estadísticas Híbridas (SQL + NoSQL)
- `GET /api/usuario/<id>/estadisticas` - Estadísticas combinadas del usuario
  - **MongoDB**: Datos del usuario, leads, asesorías
  - **SQLite**: Logs de interacciones con SYRA
