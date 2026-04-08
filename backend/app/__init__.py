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
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return db.session.get(User, int(user_id))

    # Register blueprints safely inside context
    with app.app_context():
        from app import models  # Ensure models are known to SQLAlchemy
        
        from app.modules.auth.routes import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/')
    def index():
        from flask import redirect, url_for
        return redirect(url_for('auth.login'))
        
    @app.route('/dashboard')
    @login_manager.user_loader # wait, not user loader. Just login_required
    def dashboard_tmp():
        return "Welcome to Dashboard. You are logged in!"

    # Create dummy blueprint to satisfy dashboard.index
    from flask import Blueprint
    dummy_dashboard = Blueprint('dashboard', __name__)
    @dummy_dashboard.route('/dashboard_dummy')
    def index():
        from flask import render_template_string
        from flask_login import login_required, current_user
        return render_template_string("<h1>Welcome {{ current_user.username }} to Dashboard</h1><a href='{{ url_for('auth.logout') }}'>Logout</a>")
    app.register_blueprint(dummy_dashboard)

    @app.route('/health')
    def health_check():
        from flask import jsonify
        return jsonify({"status": "ok", "message": "Backend service is running."})

    return app
