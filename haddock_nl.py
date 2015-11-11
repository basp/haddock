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

exlamations = [
	'drie duizend bommen en granaten',
	'heb je nou ooit',
	'donder en hagel',
	'duizend miljard laserstralen',
	'duizend bliksembommen',
	'duizend millioen bommen en granaten',
	'honderdduizend miljoen bommen en granaten',
	'duizend bomgranaten',
	'alle mensen',
	'tienduizend miljard bliksembommen',
	'verdikkeme',
	'verdikkie',
	'wel allemachtig',
	'wel alle mensen'
]	 

def random_curse():
	ai = random.randint(0, len(adjectives) - 1)
	ni = random.randint(0, len(nouns) - 1)
	return [adjectives[ai], nouns[ni]]
	
def random_curse2():
	ai1 = random.randint(0, len(adjectives) - 1)
	ai2 = random.randint(0, len(adjectives) - 1)
	while ai2 == ai1:
		ai2 = random.randint(0, len(adjectives) - 1)
	ni = random.randint(0, len(nouns) - 1)
	return [adjectives[ai1], adjectives[ai2], nouns[ni]]
	
def random_curse3():
	p = random.randint(0, 100)
	if p > 66:
		i = random.randint(0, len(exlamations) - 1)
		return [exlamations[i]]
	else:
		return random_curse2()
	
if __name__ == '__main__':
	curse = random_curse3()
	msg = 'Haddock vloekt: %s!' % ' '.join(curse)
	print(msg)