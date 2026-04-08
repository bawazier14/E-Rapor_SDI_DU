import os
from flask import Flask, jsonify, redirect, url_for, render_template_string
from flask_login import login_required
from app.extensions import db, migrate, login_manager, csrf

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
    csrf.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return db.session.get(User, int(user_id))

    # Register blueprints safely inside context
    with app.app_context():
        from app import models  # Ensure models are known to SQLAlchemy
        
        from app.modules.auth.routes import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

        from app.modules.users.routes import users_bp
        app.register_blueprint(users_bp, url_prefix='/users')

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    @app.route('/dashboard')
    @login_required
    def dashboard_tmp():
        return render_template_string('''
        {% extends "layouts/base.html" %}
        {% block title %}Dashboard - E-Rapor SD{% endblock %}
        {% block content %}
        <div class="container py-4">
            <h2 class="fw-bold">Dashboard</h2>
            <p class="text-muted">Selamat datang, {{ current_user.username }}!</p>
        </div>
        {% endblock %}
        ''')

    @app.route('/health')
    def health_check():
        return jsonify({"status": "ok", "message": "Backend service is running."})

    return app
