from collections import deque, namedtuple
import re
import random

class Test:
	def __init__(self, msg):
		self.msg = msg
		
	def __call__(self):
		print(self.msg)
		return [True, None]

def update():
	global actions
	while len(actions) > 0:
		action = actions[0]
		done, alternative = action()
		while alternative:
			actions.popleft()
			action = alternative
			actions.appendleft(action)
			done, alternative = action()
		if done: actions.popleft()
		
actions = deque([Test('foo'), Test('bar')])	

update()
