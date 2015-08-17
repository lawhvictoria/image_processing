import vector_math
import collisions
import math
from data import *
from cast import *
import utility

print 'P3'
print '1024 768'
print '255'

ambient_color = Color(1.0, 1.0, 1.0)
min_x = -10.0
max_x = 10.0
min_y = -7.5
max_y = 7.5
width = 1024
height = 768
eye_point = Point(0.0, 0.0, -14.0)
sphere1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05))
sphere2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4,0.4, 0.5, 0.05))
sphere_list = [sphere1, sphere2]
cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_color, Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5)))

