import vector_math
import collisions
import math
from data import *
from cast import *
import utility
from commandline import *
from sys import *


def main():
   command = commandline(argv)

   eye_point = command[1]   

   light = command[3]

   ambient_color = command[4]

   min_x = command[2][0]
   max_x = command[2][1]
   min_y = command[2][2]
   max_y = command[2][3]
   width = command[2][4]
   height = command[2][5]

   sphere_list = []
   line_count = 0
   f = open(argv[1], 'r')
   for line in f:
      line_count += 1
      try:
         sphere = line.split()
         s = Sphere(Point(float(sphere[0]), float(sphere[1]) ,float(sphere[2])), float(sphere[3]),
                    Color(float(sphere[4]), float(sphere[5]), float(sphere[6])),
                    Finish(float(sphere[7]), float(sphere[8]), float(sphere[9]), float(sphere[10])))
         sphere_list.append(s)
      except:
         print "malformed sphere on line" + str(line_count) + " ... skipping"

   cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_color, light)
            

if __name__ == '__main__':
   main()
