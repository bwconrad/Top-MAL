##---------- Modules for extracting data from MAL pages ----------##

import requests as req
from bs4 import BeautifulSoup
from modules.other import *
from modules.entry import *

# Get the HTML content of the page
def getHTML(link):
	string = req.get(link) # Retrieves the link's HTML as a string
	if(not string.status_code == req.codes.ok): # Check if request was sucessful
		string.raise_for_status()

	soup = BeautifulSoup(string.text, 'html.parser') # Converts the string into a BeautifulSoup Object
	return soup

# Get the HTML content for the specified show type (TV, Movie, OVA)
def getTypeHTML(soup, a_type):
	# Shows starting that season, NO CONTINUING 
	if(a_type == 'tv'):
		soup = soup.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-1 clearfix')

	elif(a_type == 'ona'):
		soup = soup.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-5 clearfix')

	elif(a_type == 'ova'):
		soup = soup.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-2 clearfix')

	elif(a_type == 'movie'):
		soup = soup.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-3 clearfix')

	elif(a_type == 'special'):
		soup = soup.find('div', class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-4 clearfix')
	
	return soup

# Make the Show List from the given HTML
# Returns a list for an individual season 
def makeShowList(soup):
	showList = []
	tags = soup.find_all('div', class_='seasonal-anime js-seasonal-anime') # Gets the whole tag for each entry
	for i in range(len(tags)):
		name = getName(tags[i])
		id = getID(tags[i])
		score = getScore(tags[i])
		members = getMembers(tags[i])
		image = getImage(tags[i])
		showList.append(Entry(name, score, id, members, image))
	
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
	long_image = tag.find('img')['data-srcset'] # Contains both 1x and 2x images
	return long_image.partition(' ')[0] # Only return 1x image