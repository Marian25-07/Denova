# Denova


API REST desarrollada con Flask para la gestión de usuarios, leads, asesorías y automatización básica con SYRA.



## 📦 Requisitos

Antes de empezar, se necesita tener instalado:

* Python (3.8 o superior)
* Git



## 1. Clonar el repositorio

Abre la terminal y ejecuta:

```bash
git clone https://github.com/TU-USUARIO/api-denova.git
```

Luego entra a la carpeta:

```bash
cd api-denova
```



##  2. Crear entorno virtual

```bash
python -m venv venv
```



##  3. Activar entorno virtual

### Windows (PowerShell)

```bash
.\venv\Scripts\activate
```

### Windows (CMD)

```bash
venv\Scripts\activate
```



## 4. Instalar dependencias

```bash
pip install flask
```

*(o si existe requirements.txt)*

```bash
pip install -r requirements.txt
```

---

## 5. Ejecutar el proyecto

```bash
python app.py
```



## 6. Abrir en el navegador

Ir a:

```
http://localhost:5000
```



## 7. Probar endpoints

Ejemplo crear usuario:

```bash
curl -X POST http://localhost:5000/api/usuarios \
-H "Content-Type: application/json" \
-d "{\"nombre\":\"Test\"}"
```



## Endpoints disponibles

* `/api/usuarios`
* `/api/leads`
* `/api/asesorias`
* `/api/syra`

---

## Notas

* El proyecto usa una base de datos simulada (listas en memoria)
* Al reiniciar el servidor, los datos se pierden
* Está pensado para pruebas y demostración

---

## Autor

Proyecto desarrollado como parte de la solución Denova
