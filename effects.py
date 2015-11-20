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

class Emitter:
	def __init__(self, x = 0.0, y = 0.0):
		self.x = x
		self.y = y
		self.particles = []
		
	def update(self, bounds):
		w, h = bounds
		self.x = random.randint(0, w - 1)
		self.y = random.randint(0, h - 1)
		#self.y = int(h / 2)
		#self.x = random.randint(0, w)
		alive = lambda x: x.energy > 0.05
		self.particles = filter(alive, map(self._update_particle, self.particles))
		col = [1.0, 1.0, 1.0]
		#dx = random.random() * 2.0 - 1.0
		#dy = random.random() * 2.0 - 1.0
		dx = 0
		dy = -1
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
		
