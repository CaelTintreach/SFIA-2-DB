import requests
import unittest
import requests_mock
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
	def create_app(self):
		return app

class TestUI(TestBase):
	def test_home(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)

class TestReturn(TestBase):
		def test_return(self):
			with self.client:
				with requests_mock.Mocker() as r:
					r.get('http://lgen:5001/prize/lgen', text='A')
					r.get('http://ngen:5002/prize/ngen', text='A')
					r.post('http://pgen:5003/prize/pgen', json={'Letter':'A', 'Number':'A'})                
					response = self.client.get(url_for('prize'))
					self.assertEqual(response.status_code, 200)