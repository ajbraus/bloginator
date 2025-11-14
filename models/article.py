from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255))
    body = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Article {self.title}>'