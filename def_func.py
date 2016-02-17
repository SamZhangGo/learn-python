#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def emptyFunc():
	pass

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
	
emptyFunc()
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)