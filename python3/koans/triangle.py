#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    
    if  (a + b < c) or (b + c < a) or (a + c < b):
        raise TriangleError('Sum of any 2 sides must be > the the 3rd.')


    sides = set([a, b, c])
    for s in sides:
        if s <= 0:
            raise TriangleError('Sides must all be > 0')
    
    if len(sides) == 1:
        return 'equilateral'
    if len(sides) == 2:
        return 'isosceles'
    if len(sides) == 3:
        return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
