from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login' 

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SECRET_KEY'] = 'mysecretkey'
    
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from app.models import User  # Import here to avoid circular import
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
