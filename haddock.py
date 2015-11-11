import random

adjectives = [
	'rotten',
	'lubberly',
	'thundering son of a',
	'misguided',
	'arabian',
	'dunderheaded',
	'interplanetary-pirate of a',
	'interplanetary',
	'fancy-dress',
	'cyclotron',
	'miserable molecule of a'	
]

nouns = [
	'pirate',
	'doryphore'
	'gobbledygook',
	'filibusters',
	'slubberdegullion',
	'patagonian',
	'vampire',
	'sycophant',
	'kleptomaniac',
	'egoist',
	'tramp',
	'monopolizer',
	'pockmark',
	'belemnite',
	'crook',
	'miserable earthworm',
	'coconut',
	'harlequin',
	'parasite',
	'macrocephalic baboon',
	'brute',
	'guano gatherer',
	'pachyrhizus',
	'toad',
	'gyroscope',
	'bougainvillea',
	'bloodsucker',
	'nincompoop',
	'shipwrecker',
	'cyclone',
	'gallows-fodder',
	'politician'
]

def random_curse():
	ai, ni = random.randint(0, 100), random.randint(0, 100)
	ai = ai % len(adjectives)
	ni = ni % len(nouns)
	return [adjectives[ai], nouns[ni]]
	
if __name__ == '__main__':
	curse = random_curse()
	msg = 'Haddock yells: %s' % ' '.join(curse)
	print(msg)
