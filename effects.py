from collections import namedtuple
import math
import random

class Vector:
	def __init__(self, components):
		self.components = components
		
	def len(self):
		f = lambda x: x * x
		return math.sqrt(sum(map(f, self.components)))
		
	def normalize(self):
		length = self.len()
		f = lambda x: x / length
		return Vector(map(f, self.components)) 
		
	def __str__(self):
		return str(self.components)
		
Particle = namedtuple('Particle', ['x', 'y', 'col', 'direction', 'energy'])

class Translate:
	def __init__(self, direction = Vector([0,0])):
		self.v = direction.normalize()
				
	def __call__(self):
		pass

class Emitter:
	def __init__(self, pos):
		self.x, self.y = pos
		self.particles = []
		
	def update(self, bounds):
		# Update own state
		w, h = bounds
		self.x = random.randint(0, w - 1)
		self.y = random.randint(0, h - 1)
		#self.y = int(h / 2)
		#self.x = random.randint(0, w)
		
		# Update particle state
		alive = lambda x: x.energy > 0.05
		self.particles = filter(alive, map(self._update_particle, self.particles))
		col = [1.0, 1.0, 1.0]
		
		# Translate vector components into -1.0 to 1.0 range
		dx = random.random() * 2.0 - 1.0
		dy = random.random() * 2.0 - 1.0
		direction = Vector([dx, dy]).normalize()
		
		p = Particle(
			x = self.x, 
			y = self.y, 
			col = col, 
			direction = direction, 
			energy = 1.0)
		self.particles.append(p)

	def _update_particle(self, p):
		fade = 0.9
		energy = p.energy * fade
		x = p.x + p.direction.components[0]
		y = p.y + p.direction.components[1]
		return Particle(x, y, p.col, p.direction, energy)
		
