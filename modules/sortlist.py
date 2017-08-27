##---------- Methods for sorting compiled lists ----------##

def sortByScore(arr):
	return sorted(arr, reverse=True, key=lambda x: x.score)

def sortByMembers(arr):
	return sorted(arr, reverse=True, key=lambda x: int(x.members))