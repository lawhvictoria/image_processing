from collisions import *
from vector_math import *
import math
from data import*
import utility

def cast_ray(ray, sphere_list, ambient_color, light, point):
   intersection_list = find_intersection_points(sphere_list, ray)
   if intersection_list == []:
         return Color(1.0, 1.0, 1.0)
   
   point_1 = intersection_list[0]
   smallest = length_vector(vector_from_to(ray.pt, intersection_list[0][0]))
   for p in intersection_list:
      if length_vector(vector_from_to(ray.pt, p[0])) < smallest:
         point_1 = p 

   original_color = point_1[1].color

   ambient_color = Color(point_1[1].color.r * point_1[1].finish.ambient * ambient_color.r,
                         point_1[1].color.g * point_1[1].finish.ambient * ambient_color.g,
                         point_1[1].color.b * point_1[1].finish.ambient * ambient_color.b)

   N = sphere_normal_at_point(point_1[1],point_1[0])
   scaled = scale_vector(N, 0.01)
   pe = translate_point(point_1[0], scaled)
   Ldir = normalize_vector(vector_from_to(pe, light.point))
   LdotN = dot_vector(N, Ldir)

   diffuse = Color(LdotN * light.color.r * original_color.r * point_1[1].finish.diffuse,
                   LdotN * light.color.g * original_color.g * point_1[1].finish.diffuse,
                   LdotN * light.color.b * original_color.b * point_1[1].finish.diffuse)

   diffuse_color = Color(ambient_color.r + diffuse.r,
                         ambient_color.g + diffuse.g,
                         ambient_color.b + diffuse.b)

   shadow = find_intersection_points(sphere_list, Ray(pe, Ldir))

   eye_point_1 = vector_from_to(point, pe)
   result_vector = scale_vector(N, (2 * LdotN))
   reflection = difference_vector(Ldir, result_vector)
   Vdir = normalize_vector(eye_point_1)
   specular = dot_vector(reflection, Vdir)

   specular_color = Color(diffuse_color.r + light.color.r * point_1[1].finish.specular * specular**(1 / point_1[1].finish.roughness),
                          diffuse_color.g + light.color.g * point_1[1].finish.specular * specular**(1 / point_1[1].finish.roughness),
                          diffuse_color.b + light.color.b * point_1[1].finish.specular * specular**(1 / point_1[1].finish.roughness))

   if specular > 0 and shadow == []:
      return specular_color

   elif LdotN > 0 and shadow == []:
      return diffuse_color

   else:
      return ambient_color

def print_color(color):
   if color < 1.0:
      return str(int((color)*255))
   else:
      return "255"

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_color, light):
   dx = (max_x - min_x) / float(width)
   dy = (max_y - min_y) / float(height)
   image = open('image30.ppm', 'w')
   image.write('P3\n')
   image.write(str(width)+'\n')
   image.write(str(height)+'\n')
   image.write('255\n')
   for y in range(height):
      y_point = max_y - y*dy
      for x in range(width):
         x_point = min_x + x*dx
         pixel = Point(x_point, y_point, 0)
         ray = Ray(eye_point, vector_math.vector_from_to(eye_point, pixel))
         color = cast_ray(ray, sphere_list, ambient_color, light, eye_point)
         image.write(print_color(color.r) + ' ')
         image.write(print_color(color.g) + ' ')
         image.write(print_color(color.b) + '\n')
   image.close()
