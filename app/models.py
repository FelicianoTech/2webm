from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

class Media(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text)
	url = db.Column(db.String(200))

	def __init__(self, title, url):
		self.title = title 
		self.url = url 