##---------- Server side data gathering for Top MAL -----------##
## Takes in search parameters from client and returns a JSON   ##
## files with an ordered  list with attributes to be displayed.##

from modules.client import *
from modules.tuple import *
from flask import Flask, jsonify, g, redirect, request, url_for, render_template
import json
import sys

app = Flask(__name__)

# On startup send to  main html page
@app.route('/')
def index():
    return redirect(url_for('static', filename='topmal.html'))


# Accept JSON file from client and return response in JSON
@app.route('/result', methods = ['POST', 'GET'])
def result():
	print("received", file=sys.stdout)
	
	
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

	print("sent", file=sys.stdout)
	return json.dumps(requestedList)

'''
def main():
	
	list = getYearRange(1998, 1999, [False, False, False, True, False])
	list = sortByScore(list)

	for i in range(len(list)):
		print(list[i].name + ' ' + list[i].score + ' ' + list[i].id + ' ' + list[i].members  + ' ' + list[i].season) #+ ' ' + #list[i].image

if __name__ == '__main__':
    main()
 '''