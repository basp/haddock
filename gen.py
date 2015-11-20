import random

WIDTH = 80
HEIGHT = 25

def rotate(m):
	return zip(*m[::-1])
	
def score(f, p, m):
	# We are pessimistic here and assume the feature will be 
	# Guilty unless proven innocent! The checks below will 
	# have to flag it once they hit dirt (see below).
	overlapping_feature = True
	s = 0
	rows = len(f)
	for i in range(rows):
		cols = len(f[i])
		for j in range(cols):
			# Translate the local feature into global map coordinates
			x, y = p
			x += j
			y += i
			
			# Invalid position if any feature tile is out of bounds
			if y >= HEIGHT:
				return 0
			elif x >= WIDTH:
				return 0
			
			# Ignore the feature tile if it's just dirt
			if f[i][j] == '~':
				continue

			# Increase score of we have an overlapping door or exit
			if f[i][j] == 'X' or f[i][j] == 'D':
				if m[y][x] == 'X' or m[y][x] == 'D':
					s += 1
					continue
				elif m[y][x] != '~':
					return 0
			
			# Make sure any walls are either overlapping or on dirt
			if f[i][j] == '#':
				if m[y][x] == '#':
					continue
				elif m[y][x] != '~':
					return 0
				
			# Make sure we hit a dirt tile on the map to prevent
			# scoring completely overlapping features
			if m[y][x] == '~':
				overlapping_feature = False
			else:
				return 0

	return 0 if overlapping_feature else s	
	
def top_scorers(scores):
	t = list(scores)
	t.sort()
	t.reverse()
	top_score = 0
	for (s, p) in t:
		if s >= top_score:
			top_score = s
			yield p
		else:
			break
				
def find_candidates(f, m):
	for y in range(len(m)):
		for x in range(len(m[y])):
			p = x, y
			s = score(f, p, m)
			if s > 0: 
				yield (s, p)

# This assumes a valid position (e.g. overlapping exit(s) and/or walls)
def place(f, p, m):
	rows = len(f)
	for i in range(rows):
		cols = len(f[i])
		for j in range(cols):
			# Translate the local feature into global map coordinates
			x, y = p
			x += j
			y += i
			
			# Merge feature tile with map tile
			# Doors have priority; open exits get merged into open space
			if f[i][j] == 'D':
				# Feature tile is a door
				m[y][x] == 'D'
			elif m[y][x] == 'D':
				# The map tile is already a door
				continue
			elif f[i][j] == '~':
				# Feature tile is dirt, ignore
				continue
			elif f[i][j] == 'X' and m[y][x] == 'X':
				# Feature is an exit, merge into open space
				m[y][x] = '.'
			else:
				# Replace map tile with feature tile
				m[y][x] = f[i][j]		

def try_place_feature(f, m):
	scores = list(find_candidates(f, m))
	if len(scores) == 0:
		return False, None
	best = list(top_scorers(scores))
	pos = random.choice(best)
	place(f, pos, m)
	return True, pos

def print_map(m, hide_dirt = False):
	rows = len(m)
	for y in range(rows):
		r = ''.join(m[y])
		if hide_dirt: r = r.replace('~', ' ')
		print(r)	
		
def remove_redundant_exits(m):
	rows = len(m)
	for y in range(rows):
		cols = len(m[y])
		for x in range(cols):
			if m[y][x] == 'D' or m[y][x] == 'X':
				if y == 0 or y == len(m) - 1:
					# Make any top or bottom edge tiles walls
					m[y][x] = '#'
				elif x == 0 or x == len(m[y]) - 1:
					# Make any left or right edge tiles walls
					m[y][x] = '#'
				elif m[y - 1][x] == '.' and m[y + 1][x] == '.':
					
					continue
				elif m[y][x - 1] == '.' and m[y][x + 1] == '.':
					continue
				else:
					m[y][x] = '#'

f1 = [
	['#', '#', 'X', '#', '#'],
	['#', '.', '.', '.', '#'],
	['X', '.', '.', '.', 'X'],
	['#', '.', '.', '.', '#'],
	['#', '#', 'X', '#', '#']]
	
f2 = [
	['#', '#', 'X', '#', '#', '#', 'X', '#', '#'],
	['X', '.', '.', '.', '.', '.', '.', '.', 'X'],
	['#', '#', 'X', '#', '#', '#', 'X', '#', '#']]

f3 = [
	['~', '~', '~', '#', 'X', '#', '~', '~', '~'],
	['~', '#', '#', '#', '.', '#', '#', '#', '~'],
	['~', '#', '.', '.', '.', '.', '.', '#', '~'],
	['#', '#', '.', '.', '.', '.', '.', '#', '#'],
	['#', '.', '.', '.', '.', '.', '.', '.', '#'],
	['X', '.', '.', '.', '.', '.', '.', '.', 'X'],
	['#', '.', '.', '.', '.', '.', '.', '.', '#'],
	['#', '#', '.', '.', '.', '.', '.', '#', '#'],
	['~', '#', '.', '.', '.', '.', '.', '#', '~'],
	['~', '#', '#', '#', '.', '#', '#', '#', '~'],
	['~', '~', '~', '#', 'X', '#', '~', '~', '~']]

f4 = [
	['#', '#', 'X', '#', '#'],
	['#', '.', '.', '.', '#'],
	['#', '.', '.', '.', '#'],
	['X', '.', '.', '.', 'X'],
	['#', '.', '.', '.', '#'],
	['#', '.', '.', '.', '#'],
	['#', '#', 'X', '#', '#']]
	
f5 = [
	['#', '#', '#'],
	['#', '.', 'X'],
	['#', '.', '#'],
	['#', '.', '#'],
	['#', '.', '#'],
	['#', '.', '#'],
	['#', '.', '#'],
	['X', '.', '#'],
	['#', '#', '#']]	

f6 = [
	['#', 'X', '#'],
	['#', '.', '#'],
	['#', '.', 'X'],
	['#', '.', '#'],
	['#', '.', '#'],
	['#', '.', '#'],
	['X', '.', 'X'],
	['#', '.', '#'],
	['#', 'X', '#']]	


level = [['~' for x in range(WIDTH)] for y in range(HEIGHT)]

# Seed the map with a room containing at least one exit
place(f5, (10, 10), level)

# If we can't fit a feature it goes here
failures = []

# Add some number of features (or try at least)
features = [f1, f1, f5, rotate(f5), f6, rotate(f6)]
NUM_FEATURES = 20
for x in range(NUM_FEATURES):
	f = random.choice(features)
	ok, pos = try_place_feature(f, level)
	if not ok:
		failures.append(f) 

print_map(level, True)
print("failed features: %d" % len(failures))