from models import db, connect_db, Pet

def seed_db(app):
    """function to call and seed the database"""

    #re-create all tables
    with app.app_context():
        db.drop_all()
        db.create_all()
        Pet.query.delete()
        
        pet1 = Pet(name="Woofly", species="dog", photo_url="https://sparkonus.com/wp-content/uploads/2022/06/cropped-image-2688.png", age=3, notes="Incredibly adorable.", available=True)
        pet2 = Pet(name="Porchetta", species="porcupine", photo_url="http://kids.sandiegozoo.org/sites/default/files/2017-12/porcupine-incisors.jpg", age=4, notes="Somewhat spiky!", available=True)
        pet3 = Pet(name="Snargle", species="cat", photo_url="https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg", age=5, available=True)
        pet4 = Pet(name="Dr. Claw", species="cat", photo_url="https://www.rd.com/wp-content/uploads/2020/07/GettyImages-1200166532-e1595523145779.jpg?fit=700,1024", age=10, available=True)

        db.session.add_all([pet1,pet2,pet3,pet4])
        db.session.commit()