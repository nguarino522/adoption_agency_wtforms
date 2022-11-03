from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, default_image
from forms import AddPetForm, EditPetForm
from seed import seed_db

app = Flask(__name__)
app.config['SECRET_KEY'] = '6uar1n0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)

#seed database
seed_db(app)

#old unnecessary with seeding db above
with app.app_context():
    db.create_all()


@app.route('/')
def homepage_route():
    """default homepage route"""

    pets = Pet.query.all()
    
    return render_template("index.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet_route():
    """route handling for get and post requests for add pet form"""
    
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data
        if form.photo_url.data:
            photo_url = form.photo_url.data
            Pet.add(name, species, photo_url, age, notes)
        else:
            photo_url = default_image
            Pet.add(name, species, photo_url, age, notes)
        
        flash(f'Success! {name} the {species} has been added.')
        return redirect("/")
    else:
        return render_template("pet_add_form.html", form=form)
    

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet_route(pet_id):
    """route handling for get and post requests for edit pet form"""
    
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f'Success! {pet.name} the {pet.species} has been edited.')
        return redirect("/")
    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)