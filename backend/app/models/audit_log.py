from app.extensions import db
from app.models.base import BaseModel
from datetime import datetime

class AuditLog(BaseModel):
    __tablename__ = 'audit_logs'
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) # Nullable if action performed by system
    action = db.Column(db.String(100), nullable=False) # e.g., 'CREATE', 'UPDATE', 'DELETE'
    table_name = db.Column(db.String(50))
    record_id = db.Column(db.Integer)
    description = db.Column(db.Text)
    ip_address = db.Column(db.String(45))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    user = db.relationship('User')

    def __repr__(self):
        return f"<AuditLog {self.action} on {self.table_name}>"
