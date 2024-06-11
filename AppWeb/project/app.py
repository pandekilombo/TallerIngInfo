from flask import Flask, render_template, redirect

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

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
    return render_template('perfil.html')

@app.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')

@app.route('/historial')
def historial():
    return render_template('historial.html')

@app.route('/cerrar-sesion')
def cerrar_sesion():
    # Lógica para cerrar sesión si es necesario
    # Redirige a la página de inicio de sesión
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
