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

Actualmente el proyecto funciona con almacenamiento en memoria, pero está diseñado para evolucionar a una arquitectura híbrida:

SQL (Relacional):
Usuarios
Leads
Asesorías
Seguimiento
NoSQL (Futuro):
Conversaciones (chat / WhatsApp)
Logs de interacción (SYRA)
Eventos de usuario
Formularios dinámicos
⚙️ Funcionalidades
CRUD de usuarios
Gestión de leads
Registro de asesorías
Simulación de interacción con SYRA
Endpoints REST para integración con frontend
📦 Requisitos

Antes de empezar, se necesita tener instalado:

Python 3.8 o superior
Git
