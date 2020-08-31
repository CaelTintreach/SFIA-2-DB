import unittest
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
	def create_app(self):
		return app

class TestGen(TestBase):
	def test_home_view(self):
		response = self.client.post(
			url_for('prize'),
			json=dict(
				Number = "A",
				Letter = "A"
			),
		)
		self.assertIn(b"no prize!", response.data)
		self.assertEqual(response.status_code, 200)