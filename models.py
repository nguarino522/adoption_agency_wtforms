from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


default_image = "https://media.istockphoto.com/vectors/adopt-a-pet-concept-vector-illustration-vector-id1286489291?k=20&m=1286489291&s=612x612&w=0&h=EfiS8XyUokeo16ml6_BbFS8XdunkEttuPauHhZEy5b0="

class Pet(db.Model):
    """model for pets for app"""
    
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=default_image)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    age = db.Column(db.Integer)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        """Show info about pet"""

        p = self
        return f"<Pet name: {p.name} | species: {p.species} | photo_url: {p.photo_url} | age: {p.age} | notes: {p.notes} | available: {p.availble} >"


    