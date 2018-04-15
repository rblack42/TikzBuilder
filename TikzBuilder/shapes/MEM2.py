from .BasePart import BasePart
from .Pin import Pin
from .Pin_t import Pin_t

class MEM2(BasePart):
    
    def __init__(self):
        BasePart.__init__(self,{})
        self.h = 3
        self.w = 1
        self.x = 0
        self.y = 0
        self.yl = 1.5

        self.label = "im"

        self.points = [
            (0,0),
            (1,0),
            (1,3),
            (0,3),
        ]
        self.pins = [
            (0,1.5,'w'),
            (1,1.5,'e')
        ]
        self.pins_t = [
        ]

    def draw(self,x,y,scale,color):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        tex = []
        h = self.h
        w = self.w
        data,pin_d = BasePart.draw(self)
        tex.extend(data)
        return tex,pin_d

if __name__ == '__main__':
    mux2 = MUX2()
    print(mux2.draw())


