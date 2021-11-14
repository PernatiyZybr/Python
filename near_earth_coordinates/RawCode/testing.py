# -*- coding: utf-8 -*-
"""testing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QmzwAVN3JTgh6oHcJp2Vu7bkOZi36D-D
"""

import unittest
from math import pi
from near_earth_coordinates import cartesian2keplerian, keplerian2cartesian

class TestNEC(unittest.TestCase):
  def test_right_answer(self):
    mu = 6.67408e-11*5.9742e24
    R = 6800e3
    V = 7.79e3
    r = [R,R/100,R/100]
    v = [0,V,-V/10] 
    a,e,i,Om,w,nu = cartesian2keplerian(r,v,mu)
    r1,v1 = keplerian2cartesian(a,e,i,Om,w,nu,mu)
    #self.assertEqual(r1[0],r[0])
    #self.assertEqual(v1[0],v[0])

  def test_values(self):
    mu = 6.67408e-11*5.9742e24
    R = 6800e3
    V = 7.79e3
    r = [R,R/100,R/100]
    v = [0,V,-V/10] 
    self.assertRaises(ValueError, cartesian2keplerian, r,v,-mu)
    # keplerian2cartesian arguments = (a,e,i,Om,w,nu,mu)
    self.assertRaises(ValueError, keplerian2cartesian, -1,0.5,pi/3,pi/3,pi/3,pi/3,mu)
    self.assertRaises(ValueError, keplerian2cartesian, 1e4,-0.5,pi/3,pi/3,pi/3,pi/3,mu)
    self.assertRaises(ValueError, keplerian2cartesian, 1e4,1.5,pi/3,pi/3,pi/3,pi/3,mu)
    self.assertRaises(ValueError, keplerian2cartesian, 1e4,0.5,pi/3,pi/3,pi/3,pi/3,-mu)

  def test_types(self):
    mu = 6.67408e-11*5.9742e24
    R = 6800e3
    V = 7.79e3
    r = [R,R/100,R/100]
    v = [0,V,-V/10] 
    self.assertRaises(TypeError, cartesian2keplerian, r,v,'banana')
    self.assertRaises(TypeError, cartesian2keplerian, r,v,True)
    self.assertRaises(TypeError, cartesian2keplerian, [1,'banana',1],v,mu)
    self.assertRaises(TypeError, cartesian2keplerian, [1,1,[1,1]],v,mu)
    self.assertRaises(TypeError, cartesian2keplerian, [True,1,1],v,mu)
    self.assertRaises(TypeError, cartesian2keplerian, [1,1],v,mu)
    self.assertRaises(TypeError, cartesian2keplerian, r,[1,'banana',1],mu)
    self.assertRaises(TypeError, cartesian2keplerian, r,[1,1,[1,1]],mu)
    self.assertRaises(TypeError, cartesian2keplerian, r,[True,1,1],mu)
    self.assertRaises(TypeError, cartesian2keplerian, r,[1,1],mu)
    self.assertRaises(TypeError, keplerian2cartesian, 1e4,True,pi/3,pi/3,pi/3,pi/3,mu)
    self.assertRaises(TypeError, keplerian2cartesian, 1e4,0.5,'banana',pi/3,pi/3,pi/3,mu)
    self.assertRaises(TypeError, keplerian2cartesian, 1e4,0.5,pi/3,[1,1],pi/3,pi/3,mu)
