import libtcodpy as libtcod

SCREEN_WIDTH = 16
SCREEN_HEIGHT = 16

noise2d = libtcod.noise_new(1)
m = libtcod.heightmap_new(SCREEN_WIDTH, SCREEN_HEIGHT)

for y in range(SCREEN_HEIGHT):
	for x in range(SCREEN_WIDTH):
		n = libtcod.noise_get(noise2d, [2.0 * x / SCREEN_WIDTH - 1.0, 2.0 * y / SCREEN_HEIGHT - 1.0])
		n = (n + 1.0) / 2.0
		libtcod.heightmap_set_value(m, x, y, n)
		
for y in range(SCREEN_HEIGHT):
	for x in range(SCREEN_WIDTH):
		v = libtcod.heightmap_get_value(m, x, y)
		print(v)
		
