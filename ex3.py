import libtcodpy as libtcod
from hikari import *

class Example1:
	def __init__(self, x, y, col = vec3(1.0, 1.0, 1.0)):
		self.x = x
		self.y = y
		self.col = col
		
	def __call__(self, bounds, t = 1.0):
		pixels = [Pixel(self.x, self.y, self.col)]
		return True, pixels

FONT_FLAGS = libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD

SCREEN_WIDTH = 32
SCREEN_HEIGHT = 32

LIMIT_FPS = 20

libtcod.sys_set_fps(LIMIT_FPS)

libtcod.console_set_custom_font('consolas10x10_gs_tc.png', FONT_FLAGS)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Effects', False)

components = [Example1(10, 10)]
bounds = (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

def get_color(v3):
	f = lambda x: int(x * 255)
	#f = lambda x: random.randint(0, 255)
	return map(f, v3.components)

def render_pixel(p):
	x, y, col = p
	r, g, b = get_color(col)
	col = libtcod.Color(r, g, b)
	libtcod.console_set_char_background(0, x, y, col, libtcod.BKGND_SET)
	
while not libtcod.console_is_window_closed():
	libtcod.console_clear(0)
	still_alive = []
	for c in components: 
		alive, pixels = c(bounds, t = 1.0)
		for p in pixels: render_pixel(p) 
		if alive: still_alive.append(c)
	libtcod.console_flush()
	components = still_alive
	key = libtcod.console_check_for_keypress()
	if key.vk == libtcod.KEY_ESCAPE: break