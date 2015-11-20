import libtcodpy as libtcod
from effects import Vector, Particle, Emitter

FONT_FLAGS = libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD

WIDTH = 64
HEIGHT = 64

LIMIT_FPS = 20

libtcod.sys_set_fps(LIMIT_FPS)

libtcod.console_set_custom_font('consolas10x10_gs_tc.png', FONT_FLAGS)
libtcod.console_init_root(WIDTH, HEIGHT, 'Ex2', False)

# con = libtcod.console_new(WIDTH, HEIGHT)

pos = 0, 0
emitter = Emitter(pos) 

while not libtcod.console_is_window_closed():
	libtcod.console_clear(0)
	# render
	bounds = HEIGHT, WIDTH
	emitter.update(bounds)
	for p in emitter.particles:
		v = int(255 * p.energy)
		col = libtcod.Color(v, v, v)
		x, y = int(p.x), int(p.y)
		libtcod.console_set_char_background(0, x, y, col, libtcod.BKGND_SET)
	libtcod.console_flush()
	key = libtcod.console_check_for_keypress()
	if key.vk == libtcod.KEY_ESCAPE: break