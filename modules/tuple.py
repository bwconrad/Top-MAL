##---------- Named Tuples Definitions ----------##

from collections import namedtuple


# Show's scraped info
Entry = namedtuple('Entry','name score id members image season') 

# Client search request parameters
Search = namedtuple('Search', 'sortby start end tv movie ova ona special')