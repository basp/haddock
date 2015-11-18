import inspect
import re
from collections import namedtuple

_codemap = dict(
	s='%(who.ps)',
	S='%(who.psc', 
	p='%(who.pp)', 
	P='%(who.ppc)',
	o='%(who.po)',
	O='%(who.poc)',
	r='%(who.pr)',
	R='%(who.prc)',
	q='%(who.pq)',
	Q='%(who.pqc)')

def _prep(text):
	def replace(m):
		# Escape, should move this code
		prev = m.start() - 1
		if prev >= 0 and prev < len(text):
			if text[prev] == '%': return m.group()[1:]
	
		code = m.group(1)
		return _codemap[code] if code in _codemap else m.group()
	
	pat = r'%([a-zA-Z])'
	return re.sub(pat, replace, text)

def sub(text, **kwargs):
	def replace(m):			  
		[obj, attr] = m.groups()	
		if not obj in kwargs:
			return m.group()
		elif not hasattr(kwargs[obj], attr):
			return m.group()	
				
		v = getattr(kwargs[obj], attr)
		return v() if inspect.ismethod(v) else v
		
	# %(obj.attr)
	pat = r'%\(([a-zA-Z_][[a-zA-Z0-9_]*)\.([a-zA-Z_][a-zA-Z0-9_]*)\)'	
	return re.sub(pat, replace, _prep(text))		

def _strip_painter(style): return ''

def _css_painter(style):
	def is_reset(): return True if style.startswith('/') else False
	return '</span>' if is_reset() else '<span class="%s">' % style

def _undo_painter(style):
	return '<%s>' % style

def style(text, painter=_css_painter):
	def replace(m): return painter(m.group(1))
	pat = r'<(/|/[a-zA-Z_][a-zA-Z0-9_]*|[a-zA-Z_][a-zA-Z0-9]*)>'
	return re.sub(pat, replace, text)


class Survivor(object):
	def __init__(self, prefix=None):
		self.prefix = prefix
		
	def dname(self):
		if self.prefix:
			return 'the %s survivor' % (self.prefix)
		else:
			return 'the survivor'

class Sword(object):
	def __init__(self, prefix=None, suffix=None):
		self.prefix = prefix
		self.suffix = suffix
		
	def name(self):
		if self.prefix and self.suffix:
			return '%s sword %s' % (self.prefix, self.suffix)
		elif self.prefix:
			return '%s sword' % (self.prefix)
		elif self.suffix:
			return 'sword %s' % ( self.suffix)
		else:
			return 'sword'

Player = namedtuple('Player', ['name', 'ps', 'pp'])

if __name__ == '__main__':
	who = Player('Nanira', 'she', 'her')
	dobj = Survivor(prefix='rotting')
	iobj = Sword(prefix='sexy', suffix='of hotpantses')
	text = '[o%%%p]<blue>%(who.name)</> attacks <red>%(dobj.dname)</> with %p <green>%(iobj.name)</>!'
	msg = sub(text, who=who, dobj=dobj, iobj=iobj)
	msg = style(msg)
	print(msg)
	