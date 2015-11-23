from collections import namedtuple
import math
import random

class Vector:
	def __init__(self, components):
		self.components = components
		
	def length(self):
		square = lambda x: x * x
		return math.sqrt(sum(map(square, self.components)))
		
	def normalize(self):
		l = self.length()
		f = lambda x: x / l if l > 0 else 0
		return Vector(map(f, self.components))
		
	def __add__(self, other):
		return Vector(map(sum, zip(self.components, other.components)))

	def __str__(self):
		return str(self.components)

def vec2(x, y):	
	return Vector([x, y])

def vec3(x, y, z): 
	return Vector([x, y, z])

Pixel = namedtuple('Pixel', ['x', 'y', 'col'])
Rect = namedtuple('Rect', ['x', 'y', 'width', 'height'])

class Component:
	def __call__(self, bounds, t = 1.0):
		return []

class FadingPixel:
	def __init__(self, x, y, direction, energy = 1.0):
		self.x = x
		self.y = y
		self.direction = direction.normalize()
		self.dx = self.direction.components[0]
		self.dy = self.direction.components[1]
		self.energy = energy
		
	def __call__(self, bounds, t = 1.0):
		if self.energy < 0.05: 
			return False, []
		
		r = self.energy
		g = self.energy
		b = self.energy
		col = tut.vec3(r, g, b)
		pixels = [tut.Pixel(self.x, self.y, col)]
		self.energy *= 0.9
		self.x += self.dx
		self.y += self.dy
		return True, pixels