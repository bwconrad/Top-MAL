from flask import Flask, jsonify, g, redirect, request, url_for, render_template
import json
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('static', filename='topmal.html'))

@app.route('/result', methods = ['POST', 'GET'])
def result():
	if(request.args.get('nitems') == '3'):
		list = [['Hello', '5.00', '123', '200', 'qqqqq'], ['Bye', '3.60', '222', '600', 'wwwwww']]
		#return jsonify(request.args.get('nitems'))
		return json.dumps(list)





