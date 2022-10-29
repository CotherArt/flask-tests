from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'palabra secreta' # Frase para encriptar los POST requests
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Guarda la infomracion permanente de la session por cierto tiempo
app.permanent_session_lifetime = timedelta(days=7)

# Definir el modelo de base de datos ----------------------
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Definir las rutas de la pagina --------------------------
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/view')
def view():
    # flash(f"Numero de entradas eliminadas: {nuke()}")
    return render_template('view.html', values=users.query.all())

@app.route('/test')
def test():
    return render_template('new.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True  # Define esta session como permanente
        user = request.form['nm']
        session['user'] = user

        found_user = users.query.filter_by(name=user).first() # Buscar el usuario en la bd
        if found_user: # Si el usuario existe en la bd
            session['email'] = found_user.email
        else:
            usr = users(user, '') # Crear un nuevo registro de usuario
            db.session.add(usr) # Agregar el usuario la bd
            db.session.commit() # Guarda los cambios en la bd

        flash('Login succesfull!')
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash('Already logged in')
            return redirect(url_for('user'))
        return render_template('login.html')


@app.route('/user', methods=['POST', 'GET'])
def user():
    email = None
    if 'user' in session: # Si ya hay un usuario loggeado
        user = session['user'] # Capturar el nombre del usuario

        if request.method == 'POST': # Si se recibio un POST request
            email = request.form['email'] # Capturar el email del formulario
            session['email'] = email # Registrar el email en la session
            found_user = users.query.filter_by(name=user).first() # Buscar el usuario en la bd
            found_user.email = email # Guardar el email en la bd
            db.session.commit()
            flash("Email was saved")
        else: # Si se recibio un GET request
            if 'email' in session: # Si hay un email en la session
                email = session['email'] # Capturar el email de la sesion

        return render_template('user.html', email=email)
    else: # Si el usuario no esta loggeado
        flash('You are not logged in')
        return redirect(url_for('login')) # Abrir pagina de loggeo


@app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f'You have been logged out! {user}', 'info')

    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

def nuke(): # Elimina todos los registros de la db
    num_rows_deleted = 0
    try:
        num_rows_deleted = db.session.query(users).delete()
        db.session.commit()
    except:
        db.session.rollback()
    return num_rows_deleted

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)