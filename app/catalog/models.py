from app import db

from datetime import datetime

class Catalog(db.Model):
    __tablename__ = 'catalog'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    owner = db.Column(db.String)

    items = db.relationship('Item', backref='catalog', lazy='dynamic')

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def __repr__(self):
        return 'The id is {}, Name is {}, Owner is {}'.format(self._id, self.name, self.owner)

    def __str__(self):
        return 'The created catalog is {} with id {} and owner {}'.format(self.name, self._id, self.owner)


    def serialize(self):
        """
        Serialize
        """
        return {
            'id': self._id,
            'name': self.name,
            'owner': self.owner
        }


class Item(db.Model):
    __tablename__ = 'item'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    description = db.Column(db.String)
    owner = db.Column(db.String)

    # Relationship
    category_id = db.Column(db.Integer, db.ForeignKey('catalog._id'))

    def __init__(self, name, description, category_id, owner):
        self.name = name
        self.description = description
        self.category_id = category_id
        self.owner = owner

    def __repr__(self):
        return 'Item created --> name {} ; id {}'.format(self.name, self._id)

    def __str__(self):
        return 'Str rep -- name {} -- id {}'.format(self.name, self._id)

    def serialize(self):
        return {
            'id': self._id,
            'name': self.name,
            'description': self.description,
            'category_id': self.category_id
        }
