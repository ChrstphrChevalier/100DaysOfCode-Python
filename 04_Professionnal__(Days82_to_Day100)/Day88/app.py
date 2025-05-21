from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Coffee

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    cafes = db.session.query(Coffee).all()
    return render_template('index.html', cafes=cafes)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        coffee_name = request.form.get('cafe_name')
        address = request.form.get('address')
        website = request.form.get('website')
        wifi = request.form.get('wifi') == "yes"
        power = request.form.get('power') == "yes"
        image = request.form.get('image')

        new_coffee = Coffee(
            name=coffee_name,
            adress=address,
            website=website,
            wifi=wifi,
            prises=power,
            image_url=image
        )

        db.session.add(new_coffee)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:cafe_id>', methods=['POST'])
def delete(cafe_id):
    cafe = Coffee.query.get_or_404(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
