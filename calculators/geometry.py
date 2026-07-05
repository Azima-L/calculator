import math

# comments to partner:
# make an error handler where hyp > adj or opposite side (opp) -b
# ill do it later -a

class Rectangle:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def area(self):
        return self.num1 * self.num2
    
    def perimeter(self):
        return (self.num1 * 2) + (self.num2 * 2)
    
    def perimeter2(self):
        new_width = self.num2 / self.num1
        return (self.num1 * 2) + (new_width * 2)
    
    def diagonal_length(self):
        return math.sqrt(pow(self.num1, 2) + pow(self.num2, 2))
    
    def diagonal_length2(self):
        new_width = self.num2 / self.num1
        return math.sqrt(pow(self.num1, 2) + pow(new_width, 2))
    
    def diagonal_length3(self):
        new_width = (self.num2 - (2 * self.num1)) / 2
        return math.sqrt(pow(self.num1, 2) + pow(new_width, 2))


class Triangle:
    def __init__(self, num1=0, num2=0, num3=0):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def area(self):
        return 0.5 * self.num1 * self.num2
    
    def area2(self):
        return 0.5 * self.num1 * self.num2 * math.sin(math.radians(self.num3))
    
    def area3(self):
        s = (self.num1 + self.num2 + self.num3) / 2
        return math.sqrt(s * (s - self.num1) * (s - self.num2) * (s - self.num3))
    
    def perimeter(self):
        return self.num1 + self.num2 + self.num3
    
    def side_pythagoras(self):
        return math.sqrt(pow(self.num1, 2) + pow(self.num2, 2))

    def side_pythagoras2(self):
        return math.sqrt(pow(self.num1, 2) - pow(self.num2, 2))
    
    def side_sct_opp(self):
        return math.sin(math.radians(self.num2)) * self.num1

    def side_sct_opp2(self):
        return math.tan(math.radians(self.num2)) * self.num1
    
    def side_sct_hyp(self):
        return self.num1 / math.sin(math.radians(self.num2))
    
    def side_sct_hyp2(self):
        return self.num1 / math.cos(math.radians(self.num2))
    
    def side_sct_adj(self):
        return math.cos(math.radians(self.num2)) * self.num1
    
    def side_sct_adj2(self):
        return self.num1 / math.tan(math.radians(self.num2))

    def angle(self):
        return 180 - (self.num1 + self.num2)
    
    def angle2(self):
        return (math.sin(math.radians(self.num3)) / self.num1) * self.num2
    
    def angle3(self):
        return math.degrees(math.acos((pow(self.num2, 2) + pow(self.num3, 2) - pow(self.num1, 2)) / (2 * self.num2 * self.num3)))
    
    def angle4(self):
        return math.degrees(math.asin(self.num2/self.num1))
    
    def angle5(self):
        return math.degrees(math.acos(self.num2/self.num1))
    
    def angle6(self):
        return math.degrees(math.atan(self.num1/self.num2))


class Circle:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def area(self):
        return math.pi * pow(self.num1, 2)
    
    def area2(self):
        radius = self.num1 / (2 * math.pi)
        return math.pi * pow(radius, 2)
    
    def circumference(self):
        return 2 * math.pi * self.num1
    
    def circumference2(self):
        radius = math.sqrt(self.num1 / (math.pi))
        return 2 * math.pi * radius
    
    def diameter(self):
        return self.num1 * 2
    
    def diameter2(self):
        radius = self.num1 / (2 * math.pi)
        return radius * 2
    
    def diameter3(self):
        radius = math.sqrt(self.num1 / (math.pi))
        return radius * 2
    
    def area_of_sector(self):
        return (self.num2 / 360) * math.pi * pow(self.num1, 2)
    
    def arc_of_sector(self):
        return (self.num2 / 360) * 2 * math.pi * pow(self.num1, 2)
    
    def angle_of_sector(self):
        return (self.num2 * 360) / (math.pi * pow(self.num1, 2))
    
    def angle_of_sector2(self):
        return (self.num2 * 360) / (2 * math.pi * self.num1)
    

class Cuboid():
    def __init__(self, num1=0, num2=0, num3=0):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def volume(self):
        return self.num1 * self.num2 * self.num3
    
    def volume2(self):
        return self.num1 * self.num2
    
    def tsa(self):
        return (self.num1 * self.num2 * 2) + (self.num1 * self.num3 * 2) + (self.num2 * self.num3 * 2)
    
    def tsa2(self):
        return pow(self.num1, 2) * 6
    
    def lsa(self):
        return (2 * self.num3) * (self.num1 + self.num2)

    def lsa2(self):
        return pow(self.num1, 2) * 4
    
    def space_diagonal(self):
        return math.sqrt(pow(self.num3, 2) + pow(self.num1,2) + pow(self.num2, 2))
    

class Cone():
    def __init__(self, num1=0, num2=0, num3=0):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def volume(self): #radius & height
        return (1/3) * math.pi * pow(self.num1, 2) * self.num2
    
    def volume2(self): # height & area
        return (1/3) * self.num1 * self.num2
    
    def volume3(self): #radius & slant height
        return (1/3) * math.pi * pow(self.num1, 2) * (math.sqrt(pow(self.num2, 2) - pow(self.num1, 2)))
    
    def volume4(self): # height & slant height
        return (1/3) * math.pi * self.num1 * (pow(self.num2, 2) - pow(self.num1, 2))
    
    def tsa(self): # radius & slant height
        return (math.pi * pow(self.num1, 2)) + math.pi * self.num1 * self.num2
    
    def tsa2(self): # radius & height
        return (math.pi * pow(self.num1, 2)) + math.pi * self.num1 * (math.sqrt(pow(self.num1, 2) + pow(self.num2, 2)))
    
    def tsa3(self): #base area & slant heigth
        return self.num1 + math.pi * math.sqrt(self.num1/math.pi) * self.num2
    
    def tsa4(self): # base area & height
        return self.num1 + math.pi * math.sqrt(self.num1/math.pi) * math.sqrt((self.num1 / math.pi) + pow(self.num2, 2))
    
    def csa(self): # Radius & slant height
        return math.pi * self.num1 * self.num2
    
    def csa2(self): # Radius & height
        return math.pi * self.num1 * (math.sqrt(pow(self.num1, 2) + pow(self.num2, 2)))
    
    def csa3(self): # Base Area & slant height
        return math.pi * math.sqrt(self.num1/math.pi) * self.num2
    
    def csa4(self): # base area & height
        return math.pi * math.sqrt(self.num1/math.pi) * math.sqrt((self.num1 / math.pi) + pow(self.num2, 2))
    
    def base_area(self): # radius
        return math.pi * pow(self.num1, 2)
    
    def base_area2(self): # circumference
        return math.pi * pow(self.num1/(math.pi * 2), 2)
    
    def base_area3(self): # height & slant height
        return math.pi * (pow(self.num2, 2) - pow(self.num1, 2))
    
    def slant_height(self): # radius & height
        return math.sqrt(pow(self.num1, 2) + pow(self.num2, 2))


class Pyramid():
    def __init__(self, num1=0, num2=0, num3=0, num4=0):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4

    def volume(self): #base area & height
        return (1/3) * self.num1 * self.num2
    
    def volume(self): # length, width, height
        return (1/3) * (self.num1 * self.num2) * self.num3
    
    def volume(self): # base,height of triangular base & height of pyramid
        return (1/6) * self.num1 * self.num2 * self.num3
    
    def tsa(self): # length, width, slant height across length, slant height across width
        return (self.num1 * self.num2) + (self.num1 * self.num3) + (self.num2 * self.num4)
    
    def tsa2(self): # base & height of base, base & height of side face 1,2,3
        pass
    

class Sphere():
    def __init__(self, num1=0, num2=0, num3=0):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def volume(self): # radius
        return (4/3) * math.pi * pow(self.num1, 3)
    
    def volume2(self): # Circumference
        return (4/3) * math.pi * pow(self.num1/(2 * math.pi), 3)
    
    def area(self): # radius
        return 4 * math.pi * pow(self.num1, 2)
    
    def area2(self): # circumference
        return 4 * math.pi * pow(self.num1/(2 * math.pi), 2)
    
    def area3(self): # Volume
        return 4 * math.pi * pow(math.cbrt((3 * self.num1)/(4 * math.pi)), 2)

    
class Cylinder():
    def __init__(self, num1=0, num2=0, num3=0):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def volume(self): # r & h
        return math.pi * pow(self.num1, 2) * self.num2
    
    def volume2(self): # Base area & height
        return self.num1 * self.num2
    
    def volume3(self): # circumference & height
        return (pow(self.num1, 2) * self.num2) / (4 * math.pi)
    
    def tsa(self): # r & h
        return (2 * math.pi * pow(self.num1, 2)) + (2 * math.pi * self.num1 * self.num2)

    def tsa2(self): #base area & height
        return (2 * self.num1) + (2 * math.pi * (math.sqrt(self.num1 / math.pi)) * self.num2) 

    def tsa3(self): #circumference & height
        return (self.num1 * self.num2) + (pow(self.num1, 2)/(2 * math.pi))
    
    def csa(self): # Radius & height
        return (2 * math.pi * self.num1 * self.num2)
    
    def csa2(self): # Base area & height:
        return (2 * math.pi * (math.sqrt(self.num1 / math.pi)) * self.num2)
    
    def csa3(self): # Circumference & height:
        return self.num1 * self.num2