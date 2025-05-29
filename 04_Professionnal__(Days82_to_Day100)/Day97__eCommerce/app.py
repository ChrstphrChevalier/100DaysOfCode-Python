from flask import Flask, render_template, request, redirect, url_for
import json, os
import stripe
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'supersecretkey'

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
stripe_public_key = os.getenv("STRIPE_PUBLIC_KEY")

PRODUCTS_FILE = 'products.json'
if not os.path.exists(PRODUCTS_FILE):
    with open(PRODUCTS_FILE, 'w') as f:
        json.dump([], f)

def read_products():
    if not os.path.exists(PRODUCTS_FILE):
        return []
    with open(PRODUCTS_FILE) as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def write_products(products):
    with open(PRODUCTS_FILE, 'w') as f:
        json.dump(products, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_product = {
            "name": request.form['name'],
            "price": int(float(request.form['price']) * 100),
            "description": request.form['description'],
            "image": request.form['image']
        }
        products = read_products()
        products.append(new_product)
        write_products(products)
        return redirect(url_for('shop'))
    return render_template('create.html')

@app.route('/shop')
def shop():
    products = read_products()
    return render_template('shop.html', products=products)

@app.route('/product/<int:pid>')
def product(pid):
    products = read_products()
    return render_template('product.html', product=products[pid], pid=pid)

@app.route('/checkout/<int:pid>')
def checkout(pid):
    products = read_products()
    product = products[pid]
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': product['name'],
                    'images': [product['image']],
                },
                'unit_amount': product['price'],
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('success', _external=True),
        cancel_url=url_for('product', pid=pid, _external=True),
    )
    return render_template('checkout.html', session_id=session.id, stripe_public_key=stripe_public_key)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
