from app import app
import unittest

class BaseCase(unittest.TestCase):
	def test_language_en(self):
		client = app.test_client(self)
		response = client.get('/language/en', follow_redirects=True)
		self.assertIn(b'Hello world!', response.data)

	def test_language_zh(self):
		client = app.test_client(self)
		response = client.get('/language/zh', follow_redirects=True)
		self.assertFalse('再见！'.isascii())

	def test_language_de(self):
		client = app.test_client(self)
		response = client.get('/language/de', follow_redirects=True)
		self.assertIn(b'Hallo Welt!', response.data)

if __name__ == '__main__':
	unittest.main()