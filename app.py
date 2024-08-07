from flask import Flask, render_template, Blueprint
from os import environ as env
from api.account import account

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

# initialize the application with the blueprints, database, and other configurations
def init_app():
    app.config['SECRET_KEY'] = env.get('SECRET_KEY')
    app.register_blueprint(account, url_prefix='/api')

if __name__ == '__main__':
    init_app()
    app.run(debug=True)
