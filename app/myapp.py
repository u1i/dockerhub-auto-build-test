from bottle import Bottle, request, response
import json
from random import randint
from datetime import datetime

app = Bottle()

filepath="/app"

@app.get('/')
def do_stuff():
	with open(filepath + "/stuff.json", mode='r') as file_handle:
	        file_content = file_handle.read()
	file_handle.close()
	d1 = json.loads(file_content)
	response.content_type = 'application/json'
	return(json.dumps(d1))
