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
