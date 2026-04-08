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

if __name__ == '__main__':
    cli()
