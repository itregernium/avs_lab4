import re
from app import db

contact_tags = db.Table('contact_tags',
    db.Column('contact_id', db.Integer, db.ForeignKey('contact.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(150), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    telegram = db.Column(db.String(50), nullable=True)

    tags = db.relationship('Tag', secondary=contact_tags, lazy='subquery',
                           backref=db.backref('contacts', lazy=True))

    @staticmethod
    def validate_phone(phone):
        return re.match(r'^\+?[0-9]{7,15}$', phone)

    @staticmethod
    def validate_telegram(tg):
        if not tg: return True
        return re.match(r'^@[a-zA-Z0-9_]{5,}$', tg)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)