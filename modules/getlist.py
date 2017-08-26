##---------- Procedures for making show lists ----------##

from modules.scraping import *
from modules.other import *

def getYearRange(start, stop, show_types):
	allYears = []
	for i in range(start, stop+1):
		allYears += getYear(i, show_types)

	return allYears
	
# Make an annual list from the 4 seasonal lists
def getYear(year, show_types):
	winter = getSeason(year, 'winter', show_types)
	spring = getSeason(year, 'spring', show_types)
	summer = getSeason(year, 'summer', show_types)
	fall = getSeason(year, 'fall', show_types)
	
	return winter + spring + summer + fall

# Make a seasonal list
def getSeason(year, season, show_types):
	url = generateSeasonURL(year, season) # Generate the season's url
	html = getHTML(url) # Extract the HTML form the url
	showSeason = (season + ' ' + str(year)).title()
	seasonList = getAnimeTypes(html, showSeason, show_types[0], show_types[1], show_types[2], show_types[3], show_types[4]) # Make season list of specified types
	return seasonList

# Make a combined list of the specified types of shows
def getAnimeTypes(html, season, tv, ona, ova, movie, special):
	# Grab the specific divs for each type and then extract the entries
	if(tv):
		tvHTML = getTypeHTML(html, 'tv')
		tvList = makeShowList(tvHTML, season, 'TV')
	else:
		tvList = []

	if(ona):
		onaHTML = getTypeHTML(html, 'ona')
		onaList = makeShowList(onaHTML, season, 'ONA')
	else:
		onaList = []

	if(ova):
		ovaHTML = getTypeHTML(html, 'ova')
		ovaList = makeShowList(ovaHTML, season, 'OVA')
	else:
		ovaList = []

	if(movie):
		movieHTML = getTypeHTML(html, 'movie')
		movieList = makeShowList(movieHTML, season, 'Movie')
	else:
		movieList = []

	if(special):
		specialHTML = getTypeHTML(html, 'special')
		specialList = makeShowList(specialHTML, season, 'Special')
	else:
		specialList = []

	return tvList + onaList + ovaList + movieList + specialList

