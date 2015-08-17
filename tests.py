import unittest
import data
import math
import utility
import vector_math
import collisions
import cast

class TestData(unittest.TestCase):
# ----------------- Testing __init_ -------------------
   def test_point_1(self):
      p1 = data.Point(-1, 0, 1)
      self.assertEqual(p1.x, -1)
      self.assertEqual(p1.y, 0)
      self.assertEqual(p1.z, 1)

   def test_point_2(self):
      p2 = data.Point(-8, 5, 16)
      self.assertEqual(p2.x, -8)
      self.assertEqual(p2.y, 5)
      self.assertEqual(p2.z, 16)

   def test_vector_1(self):
      v1 = data.Vector(1.0, 0.0, 0.0)
      self.assertAlmostEqual(v1.x, 1.0)
      self.assertAlmostEqual(v1.y, 0.0)
      self.assertAlmostEqual(v1.z, 0.0)

   def test_vector_2(self):
      v2 = data.Vector(-2.3, 8.9, 25.7)
      self.assertAlmostEqual(v2.x, -2.3)
      self.assertAlmostEqual(v2.y, 8.9)
      self.assertAlmostEqual(v2.z, 25.7)

   def test_ray_1(self):
      ray1 = data.Ray(data.Point(5,4,3),data.Vector(1.0,2.1,3.2))
      self.assertEqual(ray1.pt.x, 5)
      self.assertEqual(ray1.pt.y, 4)
      self.assertEqual(ray1.pt.z, 3)
      self.assertAlmostEqual(ray1.dir.x, 1.0)
      self.assertAlmostEqual(ray1.dir.y, 2.1)
      self.assertAlmostEqual(ray1.dir.z, 3.2)

   def test_ray_2(self):
      ray2 = data.Ray(data.Point(14, 9, -22),data.Vector(5.6, 8.9, -4.5))
      self.assertEqual(ray2.pt.x, 14)
      self.assertEqual(ray2.pt.y, 9)
      self.assertEqual(ray2.pt.z, -22)
      self.assertAlmostEqual(ray2.dir.x, 5.6)
      self.assertAlmostEqual(ray2.dir.y, 8.9)
      self.assertAlmostEqual(ray2.dir.z, -4.5)

   def test_sphere_1(self):
      sphere1 = data.Sphere(data.Point(5, 47, 12), 0.2, data.Color(1.0, 1.0, 1.0))
      self.assertEqual(sphere1.center.x, 5)
      self.assertEqual(sphere1.center.y, 47)
      self.assertEqual(sphere1.center.z, 12)
      self.assertAlmostEqual(sphere1.radius, 0.2)

   def test_sphere_2(self):
      sphere2 = data.Sphere(data.Point(-89, 55, -42), 2.3, data.Color(1.0, 1.0, 1.0))
      self.assertEqual(sphere2.center.x, -89)
      self.assertEqual(sphere2.center.y, 55)
      self.assertEqual(sphere2.center.z, -42)
      self.assertAlmostEqual(sphere2.radius, 2.3)

   def test_color_1(self):
      color1 = data.Color(255, 255, 255)
      self.assertEqual(color1.r, 255)
      self.assertEqual(color1.g, 255)
      self.assertEqual(color1.b, 255)

   def test_color_2(self):
      color2 = data.Color(180, 245, 0)
      self.assertEqual(color2.r, 180)
      self.assertEqual(color2.g, 245)
      self.assertEqual(color2.b, 0)

#   def test_finish_1(self):
#      finish1 = data.Finish(0.2, 0.4)
#      self.assertEqual(finish1.ambient, 0.2)
#      self.assertEqual(finish1.diffuse, 0.4)

#   def test_finish_2(self):
#      finish2 = data.Finish(1.0, 0.7)
#      self.assertEqual(finish1.ambient, 1.0)
#      self.assertEqual(finish1.diffuse, 0.7)

   def test_light_1(self):
      light1 = data.Light(data.Point(0, 1, 2), data.Color(1.0, 0.0, 0.0))
      self.assertEqual(light1.point.x, 0)
      self.assertEqual(light1.point.y, 1)
      self.assertEqual(light1.point.z, 2)
      self.assertEqual(light1.color.r, 1.0)
      self.assertEqual(light1.color.g, 0.0)
      self.assertEqual(light1.color.b, 0.0)

   def test_light_2(self):
      light2 = data.Light(data.Point(3, -4, 8), data.Color(0.2, 0.4, 0.6))
      self.assertEqual(light2.point.x, 3)
      self.assertEqual(light2.point.y, -4)
      self.assertEqual(light2.point.z, 8)
      self.assertEqual(light2.color.r, 0.2)
      self.assertEqual(light2.color.g, 0.4)
      self.assertEqual(light2.color.b, 0.6)

# -------------------- Testing __eq__ ------------------------------

   def test_point_eq1(self):
      point1 = data.Point(0, 1, 2.0)
      point2 = data.Point(0, 1, 2.0)
      self.assertTrue(point1 == point2)

   def test_point_eq2(self):
      point3 = data.Point(-8, 9.4, 5.2)
      point4 = data.Point(-5, 9.1, 5.3)
      self.assertFalse(point3 == point4)

   def test_vector_eq1(self):
      vector1 = data.Vector(2.1, 3.5, 6.8)
      vector2 = data.Vector(2.1, 3.5, 6.8)
      self.assertTrue(vector1 == vector2)

   def test_vector_eq2(self):
      vector3 = data.Vector(-0.2, -4.6, -8.7)
      vector4 = data.Vector(-0.3, -2.4, -4.2)
      self.assertFalse(vector3 == vector4)

   def test_ray_eq1(self):
      ray1 = data.Ray(data.Point(3, 5, 8), data.Vector(2.0, 1.2, 3.6))
      ray2 = data.Ray(data.Point(3, 5, 8), data.Vector(2.0, 1.2, 3.6))
      self.assertTrue(ray1 == ray2)

   def test_ray_eq2(self):
      ray3 = data.Ray(data.Point(-7, -4.5, 6.8), data.Vector(2.3, 1.5, 1.6))
      ray4 = data.Ray(data.Point(-9, -8.5, 4.3), data.Vector(3.0, 8.2, 2.6))
      self.assertFalse(ray3 == ray4)

   def test_sphere_eq1(self):
      sphere1 = data.Sphere(data.Point(-8, -4.5, 5.2), 5.6, data.Color(1.0, 1.0, 1.0))
      sphere2 = data.Sphere(data.Point(-8, -4.5, 5.2), 5.6, data.Color(1.0, 1.0, 1.0))
      self.assertTrue(sphere1 == sphere2)

   def test_sphere_eq2(self):
      sphere3 = data.Sphere(data.Point(-7.8, -9.0, 1.1), 3.2, data.Color(1.0, 1.0, 1.0))
      sphere4 = data.Sphere(data.Point(-8.4, -6.2, 3.2), 5.4, data.Color(1.0, 1.0, 1.0))
      self.assertFalse(sphere3 == sphere4)

   def test_color_eq1(self):
      color1 = data.Color(255, 255, 255)
      color2 = data.Color(255, 255, 255)
      self.assertTrue(color1 == color2)

   def test_color_eq2(self):
      color1 = data.Color(100, 120, 160)
      color2 = data.Color(100, 120, 160)
      self.assertTrue(color1 == color2)


# -------------------- Testing vector_math --------------------------

   def test_scale_vector_1(self):
      vector1 = data.Vector(5,10,20)
      scalar = (3.0)
      vector2 = data.Vector(15.0,30.0,60.0)
      self.assertEqual(vector_math.scale_vector(vector1, scalar), vector2)

   def test_scale_vector_2(self):
      vector3 = data.Vector(-1, 0, 5)
      scalar = (-2.0)
      vector4 = data.Vector(2.0, 0.0, -10.0)
      self.assertEqual(vector_math.scale_vector(vector3, -2.0), vector4)

   def test_dot_vector_1(self):
      vector1 = data.Vector(1, 20, 15)
      vector2 = data.Vector(2, 5, 3)
      product = 147
      self.assertEqual(vector_math.dot_vector(vector1, vector2), product)

   def test_dot_vector_2(self):
      vector3 = data.Vector(-15, 21, -9)
      vector4 = data.Vector(1, -6, -8)
      product = -69
      self.assertEqual(vector_math.dot_vector(vector3, vector4), product)

   def test_length_vector1(self):
      vector1 = data.Vector(1, 2, 3 )
      length_vector = 3.7416573867739413
      self.assertAlmostEqual(vector_math.length_vector(vector1), length_vector)

   def test_length_vector2(self):
      vector2 = data.Vector(4, -5, 6)
      length_vector = 8.7749643873921226
      self.assertAlmostEqual(vector_math.length_vector(vector2), length_vector)

   def test_normalize_vector1(self):
      vector1 = data.Vector(2, 1, 3)
      normal1 = data.Vector(0.5345224838, 0.2672612419, 0.8017837257)
      self.assertEqual(vector_math.normalize_vector(vector1), normal1)

   def test_normalize_vector2(self):
      vector2 = data.Vector(0, -6, 8)
      normal2 = data.Vector(0,-0.6,0.8)
      self.assertEqual(vector_math.normalize_vector(vector2), normal2)

   def test_difference_point_1(self):
      point1 = data.Point(0, 1, 2)
      point2 = data.Point(3, 4, 5)
      difference_point = data.Vector(-3, -3, -3)
      self.assertEqual(vector_math.difference_point(point1, point2), difference_point)

   def test_difference_point_2(self):
      point3 = data.Point(5, -7, -13)
      point4 = data.Point(0, 4, 8)
      difference_point = data.Vector(5, -11, -21)
      self.assertEqual(vector_math.difference_point(point3, point4), difference_point)

   def test_difference_vector_1(self):
      vector1 = data.Vector(15, 16, 17)
      vector2 = data.Vector(4, 5, 6)
      difference_vector = data.Vector(11, 11, 11)
      self.assertEqual(vector_math.difference_vector(vector1, vector2), difference_vector)

   def test_difference_vector_2(self):
      vector3 = data.Vector(-20, -45, -99)
      vector4 = data.Vector(-12, 0, 45)
      difference_vector = data.Vector(-8, -45, -144)
      self.assertEqual(vector_math.difference_vector(vector3, vector4), difference_vector)

   def test_translate_point_1(self):
      point1 = data.Point(0, 1, 2)
      vector1 = data.Vector(3, 4, 5)
      translation = data.Point(3, 5, 7)
      self.assertEqual(vector_math.translate_point(point1, vector1), translation)

   def test_translate_point_2(self):
      point2 = data.Point(-8, 9, -4)
      vector2 = data.Vector(-3, 5, -9)
      translation = data.Point(-11, 14, -13)
      self.assertEqual(vector_math.translate_point(point2, vector2), translation)

   def test_vector_from_to_1(self):
      from_point1 = data.Point(4, 8, 7)
      to_point1 = data.Point(5, 9, 6)
      travel = data.Point(1, 1, -1)
      self.assertEqual(vector_math.vector_from_to(from_point1, to_point1), travel)

   def test_vector_from_to_2(self):
      from_point2 = data.Point(-8, 5, -6)
      to_point2 = data.Point(12, 15, -24)
      travel = data.Point(20, 10, -18)
      self.assertEqual(vector_math.vector_from_to(from_point2, to_point2), travel)

# -------------------- Testing collisions --------------------------

   def test_sphere_intersection1(self):
      sphere = data.Sphere(data.Point(0,0,.3), 2.1, data.Color(1.0, 1.0, 1.0))
      ray = data.Ray(data.Point(3, 6.1, 9.2), data.Vector(5,5,5))
      expected = None
      self.assertEqual(collisions.sphere_intersection_point(ray, sphere), expected)

   def test_sphere_intersection2(self):
      sphere = data.Sphere(data.Point (0,0,0), 5, data.Color(1.0, 1.0, 1.0))
      ray = data.Ray(data.Point(0, 2, 0), data.Vector(0,10,0))
      expected = data.Point(0, 5, 0)
      self.assertEqual(collisions.sphere_intersection_point(ray, sphere), expected)

   def test_sphere_intersection3(self):
      sphere = data.Sphere(data.Point (0,0,0), 1, data.Color(1.0, 1.0, 1.0))
      ray = data.Ray(data.Point(5, 0, 0), data.Vector (1,0,0))
      expected = None
      self.assertEqual(collisions.sphere_intersection_point(ray, sphere), expected) 

   def test_sphere_intersection4(self):
      sphere = data.Sphere(data.Point (4,5,6), 7, data.Color(1.0, 1.0, 1.0))
      ray = data.Ray(data.Point(1,2,3), data.Vector(1,2,3))
      expected = data.Point(4.08140072714, 8.16280145428, 12.2442021814)
      self.assertEqual(collisions.sphere_intersection_point(ray, sphere), expected)

   def test_sphere_intersection5(self):
      sphere = data.Sphere(data.Point (-14, -16, -18), -20, data.Color(1.0, 1.0, 1.0))
      ray = data.Ray(data.Point(-21, -5, -19), data.Vector(-8, -15, -23))
      expected = data.Point(-26.1566613757, -14.6687400795, -33.8254014552)
      self.assertEqual(collisions.sphere_intersection_point(ray, sphere), expected)

   def test_sphere_intersection6(self):
      sphere = data.Sphere(data.Point (0,0,0), 2, data.Color(1.0, 1.0, 1.0))
      ray = data.Ray(data.Point(2,0,0), data.Vector(0,5,0))
      expected = data.Point(2,0,0)
      self.assertEqual(collisions.sphere_intersection_point(ray, sphere), expected)

   def test_find_intersection_points1(self):
      sphere1 = data.Sphere(data.Point(0, -1, -2), 3, data.Color(1.0, 1.0, 1.0))
      sphere2 = data.Sphere(data.Point(-4, -5, -6), 7, data.Color(1.0, 1.0, 1.0))
      sphere3 = data.Sphere(data.Point(-10, -15, -20), 2, data.Color(1.0, 1.0, 1.0))
      sphere_list = [sphere1, sphere2, sphere3]
      ray1 = data.Ray(data.Point(12, 14, 18), data.Vector(4,6,8))
      expected = []
      self.assertEqual(collisions.find_intersection_points(sphere_list, ray1), expected)

   def test_find_intersection_points2(self):
      sphere1 = data.Sphere(data.Point(0,0,0), 3, data.Color(1.0, 1.0, 1.0))
      sphere2 = data.Sphere(data.Point(40, 50, 60), 2, data.Color(1.0, 1.0, 1.0))
      sphere3 = data.Sphere(data.Point(104, 150, 200), 8, data.Color(1.0, 1.0, 1.0))
      sphere_list = [sphere1, sphere2, sphere3]
      ray2 = data.Ray(data.Point(0,-4, 0), data.Vector(0,15,0))
      expected2 = [(data.Point(0,-3,0), sphere1)]
      self.assertEqual(collisions.find_intersection_points(sphere_list, ray2), expected2)

   def test_sphere_normal_at_point1(self):
      sphere7 = data.Sphere(data.Point(0,0,0), 1, data.Color(1.0, 1.0, 1.0))
      point10 = data.Point(0,1,0)
      normalize_vector1 = data.Vector(0,1,0)
      self.assertEqual(collisions.sphere_normal_at_point(sphere7, point10), normalize_vector1)

   def test_sphere_normal_at_point2(self):
      sphere8 = data.Sphere(data.Point(5, 10, 15), 10, data.Color(1.0, 1.0, 1.0))
      point11 = data.Point(6, 12, 13)
      normalize_vector2 = data.Vector(0.3333333333333, 0.6666666666667, -0.66666666666667)
      self.assertEqual(collisions.sphere_normal_at_point(sphere8, point11), normalize_vector2)

   def test_sphere_normal_at_point3(self):
      sphere = data.Sphere(data.Point(3,3,3), 3, data.Color(1.0, 1.0, 1.0))
      point = data.Point(5,5,5)
      normalize_vector = data.Vector(0.5773502692, 0.5773502692, 0.5773502692)
      self.assertEqual(collisions.sphere_normal_at_point(sphere, point), normalize_vector)

   def test_sphere_normal_at_point4(self):
      sphere = data.Sphere(data.Point(-7, -9, -11), -6, data.Color(1.0, 1.0, 1.0))
      point = data.Point(-4, -3, -2)
      normalize_vector = data.Vector(0.2672612419, 0.5345224838, 0.8017837257)
      self.assertEqual(collisions.sphere_normal_at_point(sphere, point), normalize_vector)

# --------------------------------- Testing Cast -------------------------------------
#   def test_cast_ray1(self):
#      sphere1 = data.Sphere(data.Point(0, -1, -2), 3, data.Color(1.0, 0.0, 0.0))
#      sphere2 = data.Sphere(data.Point(-4, -5, -6), 7, data.Color(0.0, 1.0, 0.0))
#      sphere3 = data.Sphere(data.Point(-10, -15, -20), 2, data.Color(0.0, 0.0, 1.0))
#      sphere_list = [sphere1, sphere2, sphere3]
#      ray1 = data.Ray(data.Point(12, 14, 18), data.Vector(4,6,8))
#      color = data.Color(1.0, 1.0, 1.0)
#      self.assertEqual(cast.cast_ray(ray1, sphere_list), color)
#
#   def test_cast_ray2(self):
#      sphere1 = data.Sphere(data.Point(0,0,0), 3, data.Color(1.0, 0.0, 0.0))
#      sphere2 = data.Sphere(data.Point(40, 50, 60), 2, data.Color(0.0, 1.0, 0.0))
#      sphere3 = data.Sphere(data.Point(104, 150, 200), 8, data.Color(0.0, 0.0, 1.0))
#      sphere_list = [sphere1, sphere2, sphere3]
#      ray2 = data.Ray(data.Point(0,-4, 0), data.Vector(0,15,0))
#      color = sphere1.color
#      self.assertEqual(cast.cast_ray(ray2, sphere_list), color)"""

   def test_color_1(self):
      color1 = data.Color(255, 255, 255)
      self.assertEqual(color1.r, 255)
      self.assertEqual(color1.g, 255)
      self.assertEqual(color1.b, 255)

   def test_color_2(self):
      color2 = data.Color(180, 245, 0)
      self.assertEqual(color2.r, 180)
      self.assertEqual(color2.g, 245)
      self.assertEqual(color2.b, 0)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

