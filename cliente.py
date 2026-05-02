import requests

URL = "http://127.0.0.1:5000"
s = requests.Session()

# -----------------------
# REGISTRO
# -----------------------
def registrar():
    u = input("Usuario: ")
    p = input("Password: ")

    r = s.post(f"{URL}/registro", json={
        "usuario": u,
        "password": p
    })

    print(r.json())

# -----------------------
# LOGIN
# -----------------------
def login():
    u = input("Usuario: ")
    p = input("Password: ")

    r = s.post(f"{URL}/login", json={
        "usuario": u,
        "password": p
    })

    print(r.json())

# -----------------------
# VER TAREAS (HTML EN CONSOLA)
# -----------------------
def ver_tareas():
    r = s.get(f"{URL}/tareas")

    import re

    # extraer bienvenida
    bienvenida = re.search(r"<h1>(.*?)</h1>", r.text)

    # extraer tareas
    items = re.findall(r"<li.*?>(.*?)</li>", r.text)

    print("\n--- TAREAS ---\n")

    if bienvenida:
        print(bienvenida.group(1))
        print()

    for i in items:
        print(i)
# -----------------------
# CREAR TAREA
# -----------------------
def crear():
    t = input("Tarea: ")

    r = s.post(f"{URL}/tareas", json={
        "titulo": t
    })

    print(r.json())

# -----------------------
# BORRAR TAREA
# -----------------------
def borrar():
    id = input("ID tarea: ")

    r = s.delete(f"{URL}/tareas/" + id)

    print(r.json())

# -----------------------
# LOGOUT
# -----------------------
def logout():
    r = s.post(f"{URL}/logout")
    print(r.json())

# -----------------------
# MENU
# -----------------------
while True:
    print("\n--- MENU ---")
    print("1. Registrar")
    print("2. Login")
    print("3. Ver tareas")
    print("4. Crear tarea")
    print("5. Borrar tarea")
    print("6. Logout")
    print("7. Salir")

    op = input("Opción: ")

    if op == "1":
        registrar()
    elif op == "2":
        login()
    elif op == "3":
        ver_tareas()
    elif op == "4":
        crear()
    elif op == "5":
        borrar()
    elif op == "6":
        logout()
    elif op == "7":
        break