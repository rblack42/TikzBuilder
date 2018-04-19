from .BasePart import BasePart
from .Pin import Pin
from .Pin_t import Pin_t

class MUX2(BasePart):
    
    def __init__(self):
        BasePart.__init__(self,{})
        self.h = 5
        self.w = 1
        self.x = 0
        self.y = 0
        self.yl = 1.5
        self.label = "mux"

        self.points = [
            (0,0),
            (1,0.5),
            (1,2.5),
            (0,3),
        ]

        self.pins = [
            (0,1,'w'),
            (0,2,'w'),
            (1,1.5,'e'),
        ]

        self.pins_t = [
            (0.5,0.25,'s')
        ]

    def draw(self,x,y,scale,color):
        self.scale = scale
        self.x = x
        self.y = y
        self.color = color
        tex,pin_d = BasePart.draw(self)
        return tex, pin_d
       
if __name__ == '__main__':
    mux2 = MUX2()
    print(mux2.draw())


