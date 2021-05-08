from flask import Flask, render_template, request, url_for, redirect
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # print(request.method)
    # CSRF (Cross-site Request Forgery): Solicitud de falsificación entre sitios.
  if request.method == 'POST':
    # print(request.form['usuario'])
    # print(request.form['password'])
    if request.form['usuario'] == 'admin' and request.form['password'] == '1234':
      return redirect(url_for('index'))
    else:
      return redirect(url_for('login'))
    return ''
  else:
    return render_template('auth/login.html')

def pagina_no_encontrada(error):
  return render_template('errores/404.html'), 404

def inicializar_app(config):
  app.config.from_object(config)
  csrf.init_app(app)
  app.register_error_handler(404, pagina_no_encontrada)
  return app

# python manage.py runserver