##---------- Miscellaneous Modules ----------##

import re

# Removes all whitespace before and after the string
def noWhiteSpace(string):
	return string.strip()

def noWhiteSpaceOrDecimals(string):
	return re.sub(r'\W+', '', string)

def generateSeasonURL(year, season):
	return "https://myanimelist.net/anime/season/" + str(year) + "/" + season

# Get the Anime ID from a page url
def extractAnimeID(url):
	start = 30 
	stop = url.index('/', 30)
	return url[start:stop]

# Limits the list 50 entries (if number of entries > 50)
def limitList(list):
	if(len(list)>50): # More than 50 entries
		return list[0:50]
	else: # Less than 50 entries
		return list