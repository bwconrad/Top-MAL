##---------- Server side data gathering for Top MAL -----------##
## Takes in search parameters from client and returns a JSON   ##
## file with an ordered list with attributes to be displayed.  ##

from modules.client import *
from modules.tuple import *
from flask import Flask, jsonify, g, redirect, request, url_for, render_template
import json
import sys
import time


app = Flask(__name__)

# On startup send to main html page
@app.route('/')
def index():
    return redirect(url_for('static', filename='topmal.html'))


# Accept JSON file from client and return response in JSON
@app.route('/result', methods = ['POST', 'GET'])
def result():
	print("Received client request", file=sys.stdout)
	t0 = time.time()
	# List of the search parameters
	searchRequest = Search(request.args.get('sortby'),\
					 	   int(request.args.get('start')),\
					 	   int(request.args.get('end')),\
					 	   request.args.get('tv'),\
					 	   request.args.get('movie'),\
						   request.args.get('ova'),\
						   request.args.get('ona'),\
						   request.args.get('special'))

	requestedList = getRequestedList(searchRequest)
	t1 = time.time()
	print("Response Time: " + str(t1-t0), file=sys.stdout) # Print total response time
	print("Sent response to client", file=sys.stdout)
	return json.dumps(requestedList)

