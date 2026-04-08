import os
from flask import Flask
from app.extensions import db, migrate, login_manager

def create_app(config_name=None):
    app = Flask(__name__)
    
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
        
    if config_name == 'production':
        app.config.from_object('app.config.production.ProductionConfig')
    elif config_name == 'testing':
        app.config.from_object('app.config.testing.TestingConfig')
    else:
        app.config.from_object('app.config.development.DevelopmentConfig')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db, directory='migrations')
    login_manager.init_app(app)
    
    # Needs to be implemented later when user model exists
    @login_manager.user_loader
    def load_user(user_id):
        # from app.models.user import User
        # return User.query.get(int(user_id))
        pass

    # Register blueprints safely inside context
    with app.app_context():
        # import routes / blueprints here when ready
        # from app.modules.auth.routes import auth_bp
        # app.register_blueprint(auth_bp)
        pass

    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'environment': config_name}

    return app
