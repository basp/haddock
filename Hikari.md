# Hikari
Effects toolkit for libtcod. It doesn't assume libtcod though.

	bounds = Rect(0, 0, 32, 32)
	components = [effects.Trail()]
	while True:
		still_alive = []
		for c in components:
			alive, pixels = c(bounds)
			for p in pixels: render_pixel(p)
			if alive: still_alive.append(c)
		cmponents = still_alive
		
