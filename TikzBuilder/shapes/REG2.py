from .BasePart import BasePart
from .Pin import Pin
from .Pin_t import Pin_t
from .CLK import CLK

class REG2(BasePart):
    
    def __init__(self):
        BasePart.__init__(self,{})

        self.h = 5
        self.w = 1
        self.x = 3
        self.y = 0
        self.yl = 2.5
        self.scale = 1
        self.label = 'pc'

    def draw(self,x,y,scale,color):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        tex = []
        h = self.h
        w = self.w
        self.pins = [
            (0,0.5*h,'w'),
            (w,0.5*h,'e'),
        ]
        self.pins_t = []
        self.points = [
                (0,0),
                (w,0),
                (w,h),
                (0,h),
        ]

        data,pin_d = BasePart.draw(self)
        tex.extend(data)
        return tex,pin_d

       
if __name__ == '__main__':
    reg2 = REG2()
    print(reg2.draw())

