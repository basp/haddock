from collections import namedtuple
import libtcodpy as libtcod

FONT_FLAGS = libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD

WIDTH = 32
HEIGHT = 32

LIMIT_FPS = 5

libtcod.sys_set_fps(LIMIT_FPS)

libtcod.console_set_custom_font('consolas10x10_gs_tc.png', FONT_FLAGS)
libtcod.console_init_root(WIDTH, HEIGHT, 'Ex1', False)

# con = libtcod.console_new(WIDTH, HEIGHT)

Particle = namedtuple('Particle', ['x', 'y', 'color', 'energy'])

while not libtcod.console_is_window_closed():
	libtcod.console_clear(0)
	# render
	libtcod.console_flush()
	key = libtcod.console_check_for_keypress()
	if key.vk == libtcod.KEY_ESCAPE: break