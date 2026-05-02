## IFTS 29 - Programación Sobre Redes
## Práctica Formativa N° 2 - Sistema de Gestión de Tareas con API (Flask + SQLite)
## Alumno: Andrea Purriños 
## Comisión: 3A1C26


## Descripción

Este proyecto consiste en el desarrollo de una API REST utilizando Flask que permite gestionar usuarios y tareas. El sistema incluye registro de usuarios, autenticación mediante inicio de sesión y gestión básica de tareas almacenadas en una base de datos SQLite.

Las contraseñas se almacenan de forma segura utilizando hashing, evitando su almacenamiento en texto plano.

El sistema se interactúa mediante un cliente en consola que consume los endpoints de la API.

---

## Funcionalidades

- Registro de usuarios
- Inicio de sesión con autenticación
- Cierre de sesión
- Protección de rutas mediante sesiones
- Visualización de tareas mediante un endpoint HTML protegido
- Creación de tareas
- Eliminación de tareas
- Persistencia de datos mediante SQLite

---

## Tecnologías utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Werkzeug (hash de contraseñas)
- Requests (cliente en consola)

---

## Estructura del proyecto

gestion/
│── servidor.py
│── cliente.py
│── README.md
│── images/
│ ├── post_registro_registroExitoso.jpg
│ ├── post_login_loginExitoso.jpg
│ ├── get_usuarioAutorizado.jpg
│── app.db
│── .gitignore


---

## Instalación

### 1. Clonar el repositorio

### 2. Crear entorno virtual (opcional)
python -m venv venv
venv\Scripts\activate (Windows)

### 3. Instalar dependencias
pip install flask flask_sqlalchemy werkzeug requests

---

## Ejecución

### 1. Ejecutar el servidor
python servidor.py

### 2. Ejecutar el cliente
python cliente.py

---

## Endpoints

### Registro de usuario
POST /registro

{
  "usuario": "nombre",
  "password": "1234"
}

### Inicio de sesión
POST /login

{
  "usuario": "nombre",
  "password": "1234"
}

### Cierre de sesión
POST /logout

### Obtener tareas (HTML)
GET /tareas
Devuelve un HTML con mensaje de bienvenida y listado de tareas
Requiere sesión iniciada

Cliente en consola

### El cliente permite:

1.-Registrar usuario
2.-Iniciar sesión
3.-Ver tareas (respuesta HTML mostrada en consola)
4.-Crear tareas
5.-Eliminar tareas
6.-Cerrar sesión
7.-Salir

### Seguridad
-Las contraseñas se almacenan utilizando hashing con werkzeug.security
-Se utilizan funciones:
generate_password_hash
check_password_hash

### Notas
-La autenticación se maneja mediante sesiones de Flask
-La base de datos SQLite se genera automáticamente al ejecutar el servidor
-El endpoint /tareas devuelve HTML como requisito del trabajo práctico


