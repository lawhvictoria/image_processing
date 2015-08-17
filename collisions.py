import data
import vector_math
import math
import utility

def sphere_intersection_point(ray, sphere):
   a = vector_math.dot_vector(ray.dir, ray.dir)
   b = vector_math.dot_vector(vector_math.scale_vector(vector_math.difference_point(ray.pt, sphere.center), 2), ray.dir)
   c = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - (sphere.radius ** 2)
   x = b**2 - 4*a*c
   if x < 0:
      return None
   elif x == 0:
      t = -b/2*a
      if t >= 0:
         point1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t))
         return point1
      else:
         return None
   elif x > 0:
      t1 = (-b - math.sqrt(x))/(2*a)
      t2 = (-b + math.sqrt(x))/(2*a)
      if t1 >=0 or t2 >=0:
         if t1 >= 0:
            point1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
            return point1
         else:
            point1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))
            return point1
      else:
         return None


def find_intersection_points(sphere_list, ray):
   intersection_list = []
   for sphere1 in sphere_list:
      if sphere_intersection_point(ray, sphere1) != None:
         intersection_list.append((sphere_intersection_point(ray, sphere1),sphere1))
   return intersection_list

def sphere_normal_at_point(sphere, point):
   normalized_vector = vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
   return normalized_vector

