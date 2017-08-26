##---------- Miscellaneous Modules ----------##

import re
from collections import OrderedDict


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

# Limits the list to 50 entries (if number of entries > 50)
def limitList(arr):
	if(len(arr)>50): # More than 50 entries
		return list(arr.values())[0:50]
	else: # Less than 50 entries
		return list(arr.values())

# Remove all duplicates from list
# Appears when OVAs/ONAs/Specials span over mulitiple seasons
def deleteDuplicates(arr):
	new =  OrderedDict((v[0],v) for v in arr)
	return new

# Convert types requested into boolean list
def makeTypeList(tv, movie, ova, ona, special):
	types = []

	if(tv == "true"):
		types.append(True)
	else:
		types.append(False)

	if(ona == "true"):
		types.append(True)
	else:
		types.append(False)

	if(ova == "true"):
		types.append(True)
	else:
		types.append(False)

	if(movie == "true"):
		types.append(True)
	else:
		types.append(False)

	if(special == "true"):
		types.append(True)
	else:
		types.append(False)

	return types
