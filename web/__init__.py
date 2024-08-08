from flask import Flask, render_template
from dotenv import load_dotenv
from os import environ as env
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

# initialize the application with the blueprints, database, and other configurations
def create_app():
    load_dotenv()
    app.config['SECRET_KEY'] = env.get('SECRET_KEY')
    user = quote_plus(env.get("MYSQL_DATABASE_USER"))
    password = quote_plus(env.get("MYSQL_DATABASE_PASSWORD"))
    host = quote_plus(env.get("MYSQL_DATABASE_HOST"))
    port = env.get("MYSQL_DATABASE_PORT")
    database = quote_plus(env.get("MYSQL_DATABASE_DB"))
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
    
    db.init_app(app)
    
    from api.account import account
    from web.main import main
    
    app.register_blueprint(account, url_prefix='/api')
    app.register_blueprint(main, url_prefix='/')
    
    from .models import Account, Role, AccountRoles
    create_database(app)
    
    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Database created')