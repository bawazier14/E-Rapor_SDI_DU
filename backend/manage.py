import os
from flask.cli import FlaskGroup
from app import create_app
from app.extensions import db

# Read the environment variable, or default to development
env = os.getenv('FLASK_ENV', 'development')
app = create_app(env)

cli = FlaskGroup(create_app=lambda: app)

# Custom commands can be added here
@cli.command("seed_db")
def seed_db():
    print("Seeding database (dummy function for now)...")
    # Add seed logic here

@cli.command("create_admin")
def create_admin():
    from app.models.user import User
    from app.models.role import Role
    
    admin_role = Role.query.filter_by(name='Admin').first()
    if not admin_role:
        admin_role = Role(name='Admin', description='Administrator sistem')
        db.session.add(admin_role)
        db.session.commit()
        
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', role_id=admin_role.id)
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully! (username: admin, password: admin123)")
    else:
        print("Admin user already exists!")

if __name__ == '__main__':
    cli()
