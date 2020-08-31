from application import db

class prizesgiven(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pool = db.Column(db.String(20))
	value = db.Column(db.String(20))
	prize = db.Column(db.String(20))