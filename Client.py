import urllib2, json
import pprint
pokemonNotifyListURL = "http://bhenshall.co.uk/pokemon_notify.json"

pokemonNotifyListLoaded = False
pokemonNotifyList = []


#def init():
try:
	request = urllib2.Request(pokemonNotifyListURL)
	
	# Adds a header to trick webserver into thinking i'm a user to fix caching issues
	request.add_header('User-Agent', 'Mozilla/5.0')
	response = urllib2.build_opener().open(request)
	
	pokemonNotifyList = json.loads(response.read())
	
	pokemonNotifyList = pokemonNotifyList['pokemon_notify']
	pokemonNotifyListLoaded = True
	print "INITIALISED"
except ValueError:
	print "Could not download list!"

#init()
text_file = open("test.txt", "wb")

text_file.write(str(pokemonNotifyList))


def notify_pokemon(pokemons):
	i = 0
	#pprint.pprint(pokemons)
	for p in pokemons:
		i = i + 1
		if p['pokemon_data']['pokemon_id'] in pokemonNotifyList:
			print p
			print "\n"