from application import app, db
from flask import render_template, jsonify
import requests
import json
from application.models import prizesgiven

@app.route('/', methods=['GET'])
def home():
	return render_template('home.html', title='Home')

@app.route('/get/prize', methods=['GET','POST'])
def prize():
	letter = requests.get('http://lgen:5001/prize/lgen')
	number = requests.get('http://ngen:5002/prize/ngen')
	prize = requests.post('http://pgen:5003/prize/pgen', json={'Letter':letter.text, 'Number':number.text})

	db_data_set = prizesgiven(pool=letter.text, value=number.text, prize=prize.text)
	db.session.add(db_data_set)
	db.session.commit()

	return render_template('prize.html', title='Prize', prize=prize.text)