!# -*- codeing:utf08 -*-

from math import hypot

class Vector():
	'''
	define vector 
	'''

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def __repr__(self):
		'''
		将一个对象用字符串的形式表现出来
		如果没有实现该函数，打印对象时，会是<Vector object at 0x10e100070>这种格式
		'''
		return "Vector(%r, %r)" % (self.x, self.y)

	def __abs__(self):
		return hypot(self.x, self.y)
	
	def __bool__(self):
		return bool(abs(self))
	
	def __add__(self,other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __mul__(self,scalar):
		return Vector(self.x * scalar, self.y * scalar)

