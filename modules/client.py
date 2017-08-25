##---------- Modules for receiving and sending data to the client side ----------##

from modules.getlist import *
from modules.sortlist import *
from modules.other import *

import sys
# Take the client request and give back the requested list
def getRequestedList(request):
	types = makeTypeList(request.tv, request.movie, request.ova, request.ona, request.special )
	list = getYearRange(request.start, request.end, types)

	print((list[0].name), file=sys.stdout)

	if(request.sortby == 'score'):
		sortedList = sortByScore(list)
	else:
		sortedList = sortByMembers(list)

		print((sortedList[0].name), file=sys.stdout)

	finalList = limitList(sortedList)

	print((finalList[0].name), file=sys.stdout)
	
	return finalList


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

