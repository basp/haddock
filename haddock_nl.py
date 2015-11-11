import random

adjectives = [
	'driedubbelovergehaalde',
	'donderduivelse',
	'brutale',
	'ellendige',
	'aftandse',
	'doorregen',
	'bepluimde',
	'Alpiene',
	'armzalige'	
	'blauwe',
	'donderse',
	'domme',
	'overgehaalde',
	'omgekeerde',
	'overgehaalde en omgekeerde',
	'driedubbel overgehaalde',
	'duivelse',
	'druilorige',
	'duizendbommige',
	'driedubbele',
	'rondwandelende',
	'drommelse',
	'gediplomeerde'
]

nouns = [
	'appmens',
	'baanduivel',
	'dagblinde',
	'calamiteit',
	'druifluis',
	'ectoplasma',
	'galgenaas',
	'Appenijn',
	'galgengebroed',
	'vogelverschrikker',
	'baardaap',
	'vlegel',
	'bruut',
	'beulskop',
	'bargbaar',
	'autokraat',
	'anthropopithecanthropus',
	'matroos',
	'grapjas',
	'ellendeling',
	'ellendig gedierte',
	'flauwe grapjas',
	'flessenbreker',
	'folteraar',
	'zeeschuimer',
	'guanoschachelaar',
	'gepanneerde mestbol',
	'gespuis',
	'analfabeet',
	'komkommer',
]

def random_curse():
	ai = random.randint(0, len(adjectives) - 1)
	ni = random.randint(0, len(nouns) - 1)
	return [adjectives[ai], nouns[ni]]
	
if __name__ == '__main__':
	curse = random_curse()
	msg = 'Haddock vloekt: %s!' % ' '.join(curse)
	print(msg)