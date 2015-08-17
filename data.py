import utility

class Point:
   """A class to model a point in three-dimensional space.

   Attributes: x - int
               y - int
               z - int"""

   def __init__(self,x, y, z):
       self.x = x
       self.y = y
       self.z = z

   def __eq__(self, other):
      return(utility.epsilon_equal(self.x, other.x)and
             utility.epsilon_equal(self.y, other.y)and
             utility.epsilon_equal(self.z, other.z))


class Vector:
   """A class to model a vector in three-dimensional space.

   Attributes: x - float
               y - float
               z - float"""

   def __init__(self,x, y, z):
       self.x = x
       self.y = y
       self.z = z

   def __eq__(self, other):
      return(utility.epsilon_equal(self.x, other.x)and
             utility.epsilon_equal(self.y, other.y)and
             utility.epsilon_equal(self.z, other.z))


class Ray:
   """A class to model a ray, which models the positions of spheres and a light, and moves in a single direction.

   Attributes: pt - point
               dir - vector"""
   def __init__(self, pt, dir):
       self.pt = pt
       self.dir = dir

   def __eq__(self, other):
      return(self.pt == other.pt and
             self.dir == other.dir)


class Sphere:
   """A class to model a sphere, the only visible entities in the scene.

   Attributes: center - point
               radius - float"""

   def __init__(self,center, radius, color = 0, finish = 0):
      self.center = center
      self.radius = radius
      self.color = color
      self.finish = finish

   def __eq__(self, other):
      return(self.center == other.center and
             utility.epsilon_equal(self.radius, other.radius) and
             self.color == other.color and 
             self.finish == other.finish)


class Color:
   def __init__(self, r, g, b):
      self.r = r
      self.g = g
      self.b = b
 
   def __eq__(self, other):
      return(self.r == other.r and
             self.g == other.g and
             self.b == other.b)

class Finish:
   def __init__(self, ambient, diffuse, specular, roughness):
      self.ambient = ambient
      self.diffuse = diffuse
      self.specular = specular
      self.roughness = roughness

   def __eq__(self, other):
      return(self.ambient == other.ambient and 
             self.diffuse == other.diffuse and
             self.specular == other.specular and
             self.roughness == other.roughness)

class Light:
   def __init__(self, point, color):
      self.point = point
      self.color = color

   def __eq__(self, other):
      return(self.point == other.point and
             self.color == other.color)
