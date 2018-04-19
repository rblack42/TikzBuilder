from .BasePart import BasePart
from .Pin import Pin

class BAR(BasePart):
    
    def __init__(self,pins):
        self.h = 5
        self.w = 1
        self.x = 0
        self.y = 0
        self.yl = 2.5
        self.scale = 1
        self.label = "F/D"
        self.pinset = pins

    def draw(self,x,y,scale,color):
        self.x = x
        self.y = y
        w = self.w
        h = self.h
        self.scale = scale
        self.color = color
        yl = self.yl
        label = self.label

        tex = []
        tex.extend([r'\begin{scope}[shift={(%f,%f)}]' % (x,y)])

        # add pins
        pin = Pin()
        pin_d = {}
        for p in range(len(self.pinset)):
            np = p + 1
            tex.extend(pin.draw(
                    0,
                    float(self.pinset[p]),
                    'w',
                    np,
                )
            )
            pin_d["pin%d" % np] = (x,y+float(self.pinset[p]),'w')
        for p in range(len(self.pinset)):
            np = len(self.pinset) + p + 1
            tex.extend(pin.draw(
                    w,
                    float(self.pinset[p]),
                    'e',
                    np,
                    )
            )
            pin_d["pin%d" % np] = (x+w,y+float(self.pinset[p]),'e')

        # draw shape
        draw = ''
        draw += r"\draw [fill=yellow!30] "
        draw += "(0,0)"
        draw += " -- "
        draw += "(%f,0)" % w
        draw += " -- "
        draw += "(%f,%f)" % (w,h)
        draw += " -- "
        draw += "(0,%f)" % h
        draw += ' -- cycle;'
        tex.extend([draw])
        #tex.extend([CLK(w)])
        tex.extend([r'\node at (%f,%f) {%s};' % (0.5*w*scale,yl*scale,label)])

        tex.extend([r'\end{scope}'])

        return tex,pin_d

       
if __name__ == '__main__':
    barrier = Barrier()
    print(barrier.draw())


