import os 
_basedir = os.path.absolute(os.path.dirname(__file__))

config = open("config/settings.yaml", "r") 
settings = yaml.load(config) 

connection = "mysql://%s:%s@%s:3306/%s" % (
	settings['username'], settings['password'], 
	settings['hostname'], settings['database'])