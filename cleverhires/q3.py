import math

class point(object):
  
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

def distance(A,B):
  C = points(0,0,0)
  C.x = A.x - B.x
  C.y = A.y - B.y
  C.z = A.z - B.z
  return C

def crossProduct(AB,BC):
  E = points(0,0,0)
  E.x = AB.y*BC.z - AB.z*BC.y
  E.y = AB.z*BC.x - AB.x*BC.z
  E.z = AB.x*BC.y - AB.y*BC.x
  return E

def dotProduct(X,Y):
  return X.x*Y.x + X.y*Y.y + X.z*Y.z


def modulus(X,Y):
  return math.sqrt((X.x**2+X.y**2+X.z**2)*(Y.x**2+Y.y**2+Y.z**2))


A = point(map(float , raw_input().split()))
B = point(map(float , raw_input().split()))
C = point(map(float , raw_input().split()))
D = point(map(float , raw_input().split()))

AB = distance(A,B)
BC = distance(B,C)
CD = distance(C,D)
X = crossProduct(AB,BC)
Y = crossProduct(BC,CD)

print "%.2f"%math.degrees(math.acos(dotProduct(X,Y)/modulus(X,Y)))