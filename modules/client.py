##---------- Modules for receiving and sending data to the client side ----------##

from modules.getlist import *
from modules.sortlist import *
from modules.other import *


# Take the client request and give back the requested list
def getRequestedList(request):
	types = makeTypeList(request.tv, request.movie, request.ova, request.ona, request.special )
	allEntries = getYearRange(request.start, request.end, types)

	if(request.sortby == 'score'):
		sortedList = sortByScore(allEntries)
	else:
		sortedList = sortByMembers(allEntries)

	finalList = limitList(deleteDuplicates(sortedList)) 
	return finalList



