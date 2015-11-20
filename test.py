import libtcodpy as libtcod

def noise_example():
	noise1d = libtcod.noise_new(1)
	for s in range(10):
		x = s / float(5)
		v = libtcod.noise_get(noise1d, [x])
		print(v)	
	libtcod.noise_delete(noise1d)

def handle_keys():
    key = libtcod.console_check_for_keypress()
	# key = libtcod.console_wait_for_keypress(True)

    if key.vk == libtcod.KEY_ESCAPE:
        return True

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

FONT_FLAGS = libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD

MAP_WIDTH = 80
MAP_HEIGHT = 45

LIMIT_FPS = 5

libtcod.sys_set_fps(LIMIT_FPS)

libtcod.console_set_custom_font('consolas10x10_gs_tc.png', FONT_FLAGS)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Test', False)

con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

# libtcod.console_set_char_background(con, x, y, c, libtcod.BKGND_SET)

def render_all():
	


while not libtcod.console_is_window_closed():
	render_all()
	
	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
	libtcod.console_flush()
    
	exit = handle_keys()
	
	current_map = (current_map + 1) % len(maps)
	if exit:
		break
