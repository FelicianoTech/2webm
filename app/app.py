import yaml 

from flask import Flask, render_template, request, Blueprint, session, redirect
from models import db 
import datetime 

# Configuration for the App 

config = open("config/settings.yaml", "r") 
settings = yaml.load(config) 

connection = "mysql://%s:%s@%s:3306/%s" % (
	settings['username'], settings['password'], 
	settings['hostname'], settings['database'])

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = connection 
app.secret_key = settings['secret_key']
db.init_app(app) 

with app.app_context(): 
	db.create_all()
	db.session.commit() 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')  
def home():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True) 