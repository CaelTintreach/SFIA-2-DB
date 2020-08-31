from application import app
from flask import request, Response 
import random

@app.route('/prize/ngen', methods = ['GET'])
def nGen():
	prizePool = ["A", "B"]
	return Response(random.choice(prizePool), mimetype='text/plain')