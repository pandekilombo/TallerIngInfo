from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta  # Importar timedelta para configurar sesiones permanentes

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para usar sesiones
app.permanent_session_lifetime = timedelta(days=7)  # Ejemplo: sesiones permanentes durante 7 días

# Diccionario para almacenar usuarios registrados
users = {}

# Ruta para la página principal
@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

# Ruta para la página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            session['email'] = user['email']
            
            # Si el usuario ha marcado "Recordar nombre de usuario", almacenar en sesión permanente
            if request.form.get('remember-username'):
                session.permanent = True
            else:
                session.permanent = False
            
            return redirect(url_for('home'))
        else:
            error = "Nombre de usuario o contraseña incorrectos"
            return render_template('login.html', error=error)
    return render_template('login.html')

# Ruta para la página de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        
        if password != confirm_password:
            error = "Las contraseñas no coinciden"
            return render_template('register.html', error=error)
        
        if username in users:
            error = "El nombre de usuario ya está tomado"
            return render_template('register.html', error=error)
        
        users[username] = {'password': generate_password_hash(password), 'email': email}
        flash('Usuario registrado con éxito, por favor inicia sesión.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Ruta para cerrar sesión
@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.pop('username', None)
    session.pop('email', None)
    session.permanent = False  # Asegurarse de que la sesión no sea permanente al cerrar sesión
    return redirect(url_for('login'))

# Rutas para las páginas de cada botón
@app.route('/reservar-estacionamiento')
def reservar_estacionamiento():
    return render_template('reservar_estacionamiento.html')

@app.route('/registro-estacionamientos')
def registro_estacionamientos():
    return render_template('registro_estacionamientos.html')

@app.route('/sugerencias')
def sugerencias():
    return render_template('sugerencias.html')

# Rutas para las páginas de perfil, configuración e historial
@app.route('/perfil')
def perfil():
    if 'username' in session:
        username = session['username']
        email = session['email']
        return render_template('perfil.html', username=username, email=email)
    else:
        return redirect(url_for('login'))

@app.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')

@app.route('/historial')
def historial():
    return render_template('historial.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')

if __name__ == '__main__':
    app.run(debug=True)
