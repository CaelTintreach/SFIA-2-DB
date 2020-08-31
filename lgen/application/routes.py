from application import app
from flask import request, Response 
import random

@app.route('/prize/lgen', methods = ['GET'])
def lGen():
	prizePool = ["A", "B"]
	return Response(random.choice(prizePool), mimetype='text/plain')