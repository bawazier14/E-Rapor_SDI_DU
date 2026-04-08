from app.config.default import Config

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    ENV = 'development'
    
    # Can override base database URI here if needed for dev
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:rootpassword@localhost:3306/erapor_sd'
