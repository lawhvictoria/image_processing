from sys import *
from data import *

def commandline(argv):
   error_string = " usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b] "
   if len(argv) == 1:
      print error_string   
      exit()
   else:
      try:
         f = open(argv[1], 'r')
      except:
         print "File not found!"
         exit()
      if "-eye" in argv:
         try:
            index_eye = argv.index("-eye")
            eye_point = Point(float(argv[index_eye + 1]),
                              float(argv[index_eye + 2]),
                              float(argv[index_eye + 3]))
         except:
            print "eye wrong"
            print error_string
            exit()
      else:
         eye_point = Point(0.0, 0.0, -14.0)
      if "-view" in argv:
         try:
            index_view = argv.index("-view")
            view_point = (float(argv[index_view + 1]),
                          float(argv[index_view + 2]),
                          float(argv[index_view + 3]),
                          float(argv[index_view + 4]),
                          argv[index_view + 5],
                          argv[index_view + 6])
         except:
            print "view wrong"
            print error_string
            exit()
      else:
            view_point = (-10.0, 10.0, -7.5, 7.5, 1024, 768)
      if "-light" in argv:
         try:
            index_light = argv.index("-light")
            light = Light(Point(float(argv[index_light + 1]),
                                float(argv[index_light + 2]),
                                float(argv[index_light + 3])),
                          Color(float(argv[index_light + 4]),
                                float(argv[index_light + 5]),
                                float(argv[index_light + 6])))
         except:
            print "light wrong"
            print error_string
            exit()
      else:
         light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      if "-ambient" in argv:
         try:
            index_ambient = argv.index("-ambient")
            color =  Color(float(argv[index_ambient + 1]),
                           float(argv[index_ambient + 2]),
                           float(argv[index_ambient + 3]))
         except:
            print "color wrong"
            print error_string
            exit()
      else:
         color = Color(1.0, 1.0, 1.0)

      return f, eye_point, view_point, light, color
