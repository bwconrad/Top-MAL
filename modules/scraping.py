##---------- Modules for extracting data from MAL pages using Beautiful Soup ----------##

import requests as req
from bs4 import BeautifulSoup, SoupStrainer
import time
import sys
from modules.other import *
from modules.tuple import *


import sys

# Get the HTML content of the page
def getHTML(link):
	html = req.get(link, allow_redirects=True) # Retrieves the link's HTML as a string

	# If request was unsucessful, sleep and try again
	tries = 0
	while(not html.status_code == req.codes.ok): 
		time.sleep(0.001)
		html = req.get(link, allow_redirects=True)
		tries += 1
		if(tries>10):
			time.sleep((tries-9)*5)
			print("Waiting of " + link + "GET response: " + str((tries-9)*5))

	onlyContent = SoupStrainer(id='content')
	soup = BeautifulSoup(html.text, "lxml", parse_only=onlyContent) # Converts the string into a BeautifulSoup Object

	return soup

# Get the HTML content for the specified show type (TV, Movie, OVA)
def getTypeHTML(html, a_type):
	# Shows starting that season, NO CONTINUING SHOWS
	if(a_type == 'tv'):
		soup = html.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-1 clearfix')

	elif(a_type == 'ona'):
		soup = html.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-5 clearfix')

	elif(a_type == 'ova'):
		soup = html.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-2 clearfix')

	elif(a_type == 'movie'):
		soup = html.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-3 clearfix')

	elif(a_type == 'special'):
		soup = html.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-4 clearfix')
	
	return soup

# Make the Show List from the given HTML
# Returns a list for an individual season 
def makeShowList(soup, season, showType):
	showList = []
	tags = soup.find_all('div', class_='seasonal-anime js-seasonal-anime') # Gets the whole tag for each entry
	for i in range(len(tags)):
		name = getName(tags[i])
		id = getID(tags[i])
		score = getScore(tags[i])
		members = getMembers(tags[i])
		image = getImage(tags[i])

		showList.append(Entry(name, score, id, members, image, season, showType))
	
	return showList

def getName(tag):
	return noWhiteSpace(tag.find(class_='title-text').getText())

def getID(tag):
	ref = tag.find(class_='title').a['href'] #Get the href of each show
	return extractAnimeID(ref) #Extract the ID from the href

def getScore(tag):
	score = noWhiteSpace(tag.find(class_='score').getText()) 
	if(score == 'N/A'): 
		return '0'
	else:
		return score 

def getMembers(tag):
	return noWhiteSpaceOrDecimals(tag.find(class_='member fl-r').getText())

def getImage(tag):
	# Look for 'src' attr
	try: 
		return tag.find('img')['src'] 
	except KeyError: # No 'src'
		# Look for 'data-srcset'
		try:
			long_image = tag.find('img')['data-srcset'] # Contains both 1x and 2x images
			return long_image.partition(' ')[0] # Only return 1x image
		except KeyError:
			return "NOTHING"
	#return "hello"




