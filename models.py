from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


default_image = "https://img.freepik.com/premium-vector/adopt-pet-little-dog-cat-with-adpot-me-lettering-illustration_24640-68872.jpg?w=826"

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

    @classmethod
    def add(self, name, species, photo_url, age, notes):
        """class method to make adding pet easier"""
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

