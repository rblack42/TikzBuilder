from .BasePart import BasePart
from .Pin import Pin
from .Pin_t import Pin_t

class ALU(BasePart):

    def __init__(self):
        BasePart.__init__(self,{})
        self.h = 5
        self.w = 2
        self.x = 0
        self.y = 0
        self.yl = 3.5

        self.label = "alu"
        self.points = [
            (0,0),
            (2,1),
            (2,4),
            (0,5),
            (0,3),
            (1,2.5),
            (0,2),
        ]
        self.pins = [
            (0,1,'w'),
            (0,4,'w'),
            (2,2.5,'e'),
        ]
        self.pins_t = [
            (1,0.5,'s'),
            (1,4.5,'n')
        ]
        self.anchors = []

    def draw(self,x,y,scale,color):
        self.scale = scale
        self.x = x
        self.y = y
        self.color = color
        tex,pin_d = BasePart.draw(self)
        return tex, pin_d

