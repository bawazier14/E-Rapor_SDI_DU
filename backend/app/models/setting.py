from app.extensions import db
from app.models.base import BaseModel

class Setting(BaseModel):
    __tablename__ = 'settings'
    
    key = db.Column(db.String(100), unique=True, nullable=False, index=True)
    value = db.Column(db.Text)
    description = db.Column(db.String(255))
    type = db.Column(db.String(20), default='string') # string, integer, boolean, json

    def __repr__(self):
        return f"<Setting {self.key}={self.value}>"
