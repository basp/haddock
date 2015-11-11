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
	'miserable molecule of a',
	'freshwater',
	'lily-livered',
	'meddlesome',
	'macrocephalic',
	'pestilential',
	'pithecanthropic',
	'raggle taggle',
	'squawking',
	'scoffing'
]

nouns = [
	'bootlegger',
	'bath-tub',
	'breathalyser',
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
	ai = random.randint(0, len(adjectives) - 1)
	ni = random.randint(0, len(nouns) - 1)
	return [adjectives[ai], nouns[ni]]
	
if __name__ == '__main__':
	curse = random_curse()
	msg = 'Haddock yells: %s!' % ' '.join(curse)
	print(msg)
