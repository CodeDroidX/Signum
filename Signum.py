#import math
from mpmath import *
v=3.0
print("Signum Math module v"+str(v)+" starting with default preset")
print(mp)
old_sin=sin
old_cos=cos
old_tan=tan
old_atan=atan
old_asin=asin
old_acos=acos
sin=lambda x: old_sin(radians(x))
cos=lambda x: old_cos(radians(x))
tan=lambda x: old_tan(radians(x))
atan=lambda x: degrees(old_atan(x))
asin=lambda x: degrees(old_asin(x))
acos=lambda x: degrees(old_acos(x))

class num(mpf):
    pass
Num=lambda x: num(str(x)) if type(x)==type(0.1) else num(x)

class Angle:
    def __init__(self,dir=0):
        self.value=Num(dir)
        self.normalize()
    def __repr__(self):
        return "Angle <"+str(self.value)+"°>"
    def __add__(self,degr):
        new=Angle()
        new.value+=self.value
        new.value+=degr.value
        new.normalize()
        return new
    def __sub__(self,degr):
        new=Angle()
        new.value+=self.value
        new.value-=degr.value
        new.normalize()
        return new
    def normalize(self):
        while self.value > 360:
            self.value-=360
        while self.value < 0:
            self.value+=360
class Vector:
    def __init__(self,dir=0,value=0):
        self.dir=Angle(dir)
        self.value=Num(value)
    def __repr__(self):
        return "Vector <"+str(self.dir.value)+"°,"+str(self.value)+">"
    def __add__(self,vec):
        new_pr=Project()
        new_pr.from_Vector(self)
        tmp=Project()
        tmp.from_Vector(vec)
        new_pr=new_pr+tmp
        new=Vector()
        new.from_Project(new_pr)
        return new

    def __sub__(self,vec):
        new_pr=Project()
        new_pr.from_Vector(self)
        tmp=Project()
        tmp.from_Vector(vec)
        new_pr=new_pr-tmp
        new=Vector()
        new.from_Project(new_pr)
        return new

    def from_Project(self,proec):
        x_d,y_d=proec.x,proec.y
        if x_d==0 and y_d>0: direction=Angle(0)
        elif x_d==0 and y_d<0: direction=Angle(180)
        elif y_d==0 and x_d>0: direction=Angle(90)
        elif y_d==0 and x_d<0: direction=Angle(270)
        elif y_d > 0: direction=Angle(atan(x_d/y_d))
        elif y_d < 0:
            direction=Angle(atan(x_d/y_d))+Angle(180)
        else: direction=Angle(0)
        self.dir=direction
        self.value=hypot(proec.x,proec.y)
class Project:
    def __init__(self,x=0,y=0):
        self.x=Num(x)
        self.y=Num(y)
    def __repr__(self):
        return "Projection <"+str(self.x)+";"+str(self.y)+">"
    def __add__(self,project):
        new=Project()
        new.x+=self.x
        new.y+=self.y
        new.x+=project.x
        new.y+=project.y
        return new
    def __sub__(self,project):
        new=Project()
        new.x+=self.x
        new.y+=self.y
        new.x-=project.x
        new.y-=project.y
        return new
    def from_Vector(self,vec):
        self.x=sin(vec.dir.value)*vec.value
        self.y=cos(vec.dir.value)*vec.value
