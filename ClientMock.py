# Simulates a response from the API.

from Client import notify_pokemon
pokemons = [
	{
		"last_modified_timestamp_ms":1472418556993,
		"longitude":-2.114507897981236,
		"pokemon_data":{	 
			"pokemon_id":21
		},
		"latitude":52.97815745874508,
		"spawn_point_id":u"487a6bd6ae1",
		"encounter_id":16277047887689130445,
		"time_till_hidden_ms":755225534
	},
	{
		"last_modified_timestamp_ms":1472419080248,
		"longitude":-2.0971779496880343,
		"pokemon_data":{	 
			"pokemon_id":100
		},
		"latitude":52.969904306470404,
		"spawn_point_id":u"487a6bc71e5",
		"encounter_id":9901286099355561917,
		"time_till_hidden_ms":877916
	}
]

notify_pokemon(pokemons)

pokemons = [
	{
		"last_modified_timestamp_ms":1472418556993,
		"longitude":-2.114507897981236,
		"pokemon_data":{	 
			"pokemon_id":32
		},
		"latitude":52.97815745874508,
		"spawn_point_id":u"487a6bd6ae1",
		"encounter_id":16277047887689130445,
		"time_till_hidden_ms":755225534
	},
	{
		"last_modified_timestamp_ms":1472419080248,
		"longitude":-2.0971779496880343,
		"pokemon_data":{	 
			"pokemon_id":149
		},
		"latitude":52.969904306470404,
		"spawn_point_id":u"487a6bc71e5",
		"encounter_id":9901286099355561917,
		"time_till_hidden_ms":877916
	}
]

notify_pokemon(pokemons)