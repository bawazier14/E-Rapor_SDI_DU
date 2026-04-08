from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.models.base import BaseModel

class User(UserMixin, BaseModel):
    __tablename__ = 'users'

    username = db.Column(db.String(100), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship('Role', back_populates='users')

    # One-to-one relationship bindings (set nullable=True, will be linked if User is a Guru, Siswa etc)
    guru = db.relationship('Guru', back_populates='user', uselist=False)
    siswa = db.relationship('Siswa', back_populates='user', uselist=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def has_role(self, role_name):
        return self.role and self.role.name == role_name

    def __repr__(self):
        return f"<User {self.username}>"
