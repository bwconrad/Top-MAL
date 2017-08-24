##---------- Methods for sorting compiled lists ----------##

def sortByScore(list):
	return sorted(list, reverse=True, key=lambda x: x.score)

def sortByMembers(list):
	return sorted(list, reverse=True, key=lambda x: x.members)