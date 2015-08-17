import math
import data

def scale_vector(vector, scalar):
   """This function creates (and returns) a new vector with components equal to the original vector scaled (i.e., multiplied) by the scalar argument.

      For example, vector <1, 2, 3> scaled by 1.5 will result in vector <1.5, 3, 4.5>."""

   new_vector = data.Vector(vector.x*scalar, vector.y*scalar, vector.z*scalar)
   return new_vector

def dot_vector(vector1, vector2):
   """This function performs a type of multiplication (product) on vectors. The dot product of two vectors is computed as follows.
      <x1, y1, z1> * <x2, y2, z2> = x1 * x2 + y1 * y2 + z1 * z2."""

   dot_product = (vector1.x*vector2.x + vector1.y*vector2.y + vector1.z*vector2.z)
   return dot_product

def length_vector(vector):
   """The length of a vector (i.e., its magnitude) is computed from its components using the Pythagorean theorem."""

   length = math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)
   return length

def normalize_vector(vector):
   """The function creates (and returns) a new vector by normalizing the input vector. This means that the resulting vector has the same direction but a magnitude of 1. In short, the new vector is the original vector scaled by its length."""

   length = length_vector(vector)
   normal = data.Vector(vector.x/length, vector.y/length, vector.z/length)
   return normal

def difference_point(point1, point2):
   """This function creates (and returns) a new vector obtained by subtracting from point point1 the point point2 (i.e., point1 - point2). This is computed by subtracting the corresponding x-, y-, and z-components. This gives a vector, conceptually, pointing from point2 to point1."""

   difference_point = data.Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)
   return difference_point

def difference_vector(vector1, vector2):
   """This functions creates (and returns) a new vector obtained by subtracting from vector vector1 the vector vector2 (i.e., vector1 - vector2). This is computed by subtracting the corresponding x-, y-, and z-components. (Yes, this is very similar to the previous function; the types, however, are conceptually different.)"""

   difference_vector = data.Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)
   return difference_vector

def translate_point(point, vector):
   """This function creates (and returns) a new point created by translating (i.e., moving) the argument point in the direction of and by the magnitude of the argument vector. You can think of this as the argument vector directing the new point where and how far to go from the argument point.

For example, translating point <9, 0, 1> along vector <1, 2, 3> will result in point <10, 2, 4>."""

   translation = data.Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)
   return translation

def vector_from_to(from_point, to_point):
   """This function is simply added to improve readability (and, thereby, to reduce confusion in later assignments). A vector in the direction from one point (from_point) to another (to_point) can be found by subtracting (i.e., point difference) from_point from to_point (i.e., to_point - from_point)."""

   travel = data.Vector(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)
   return travel







