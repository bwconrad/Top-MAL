##---------- Server side data gathering for Top MAL ----------##
## Takes in search parameters from client and returns ordered ##
## list with attributes to be displayed.                      ##

from modules.getlist import *
from modules.sortlist import *
from flask import Flask, jsonify, g, redirect, request, url_for, render_template
import json

'''
@app.route('/')
def index():
    return redirect(url_for('static', filename='topmal.html'))


@app.route('/result', methods = ['POST', 'GET'])
def result():
	sort = request.args.get('sort')
	startYear = requests.args.get('startYear')
	endYear = requests.args.get('endYear')


	return json.dumps(list)
'''



def main():
	
	list = getYearRange(1998, 1999, [False, False, False, True, False])
	list = sortByScore(list)

	for i in range(len(list)):
		print(list[i].name + ' ' + list[i].score + ' ' + list[i].id + ' ' + list[i].members  ) #+ ' ' + #list[i].image

if __name__ == '__main__':
    main()