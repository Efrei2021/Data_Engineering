import unittest
import requests
import os
import json
from flask import Flask

app = Flask(__name__)


class FlaskTestCase (unittest.TestCase):
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		
	def tearDown(self):
		pass
		
		
	#Enusre that Flask was setup correctly
	def test_home(self):
		tester = app.test_client(self)
		responce = tester.get('http://localhost:5000/')
		self.assertEqual(responce.status_code, 200)
		
	def test_predict(self):
		tester = app.test_client(self)
		responce = tester.get('http://localhost:5000/#')
		self.assertEqual(responce.status_code, 200)
		
			
		
	
	
if __name__ == '__main__':
	unittest.main()








