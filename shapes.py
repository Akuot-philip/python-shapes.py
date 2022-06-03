class   Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        area = 3.14*self.radius**2
        return area
    def perimeter(self):
        perimeter=2*self.radius*3.14
        return perimeter

Circle2=Circle(5)
print(Circle2.area())
print(Circle2.perimeter())        





class   Square:
    def __init__(self,a):
        self.width=a
    def area(self):
        area =self.width**2
        return area
    def perimeter(self):
        perimeter=self.width*4
        return perimeter

Square2=Square(20)
print(Square2.area())
print(Square2.perimeter()) 



class   Rectangle:
    def __init__(self,w,l):
        self.width=w
        self.length=l
    def area(self):
        area =self.width * self.length
        return area
    def perimeter(self):
        perimeter=2*self.length+self.width
        return perimeter

Rectangle2=Rectangle(30,6)
print(Rectangle2.area())
print(Rectangle2.perimeter()) 

class   Sphere:
    def __init__(self,r):
        self.radius=r
    def area(self):
        area = 4*3.14*self.radius**2
        return area
    def perimeter(self):
        perimeter=4/3*self.radius**3
        return perimeter

Sphere2=Sphere(5)
print(Sphere2.area())
print(Sphere2.perimeter())