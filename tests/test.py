import sys
sys.path.insert(0, 'PATH') //////
from modules.client import *
from modules.tuple import *
from flask import Flask, jsonify, g, redirect, request, url_for, render_template
import json


import time


t0 = time.time()

print("Received client request", file=sys.stdout)
	
# List of the search parameters
searchRequest = Search('score',\
				 	   2000,\
				 	   2010,\
				 	   'true',\
				 	   'true',\
					   'true',\
					   'true',\
					   'true')

requestedList = getRequestedList(searchRequest)



t1 = time.time()
print(t1-t0, file=sys.stdout)

print("Sent response to client", file=sys.stdout)

