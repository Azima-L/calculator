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
    pass
    

class Cone():
    pass
    

class Pyramid():
    pass
    

class Sphere():
    pass
    

class Cylinder():
    pass