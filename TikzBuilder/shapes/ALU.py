from .BasePart import BasePart
from .Pin import Pin
from .Pin_t import Pin_t

class ALU(BasePart):

    def __init__(self):
        BasePart.__init__(self,{})
        self.h = 5
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

    def draw(self,name):
        h = self.h
        scale = self.h/5.0
        x = self.x
        y = self.y
        label = name
        tex = ['data is here']
        tex.extend([r'\begin{scope}[shift={(%f,%f)}]' % (x,y)])
        # add pins
        pin = Pin()
        for p in range(len(self.pins)):
            xp = self.pins[p][0]*scale
            yp = self.pins[p][1]*scale
            sp = self.pins[p][2]
            np = p + 1
            tex.extend(pin.draw(
                    xp,
                    yp,
                    sp,
                    np
                )
            )

            # locate anchor
            if sp == "n": yp += 0.125
            elif sp == "s": yp -= 0.125
            elif sp == "e": xp += 0.125
            elif sp == "w": xp -= 0.125

            pin_anchor = {
                    "pin%d" % np: np,
                    "x":    "%d" % xp,
                    "y":    "%f" % yp
            }
        pin = Pin_t()
        for p in range(len(self.pins_t)):
            xp = self.pins_t[p][0]*scale
            yp = self.pins_t[p][1]*scale
            sp = self.pins_t[p][2]
            np = len(self.pins_t) + p + 1

            tex.extend(pin.draw(
                    xp,
                    xp,
                    xp,
                    np
                )
            )
        draw = ''
        draw += r"\draw [fill=yellow!30] "
        for i in range (len(self.points)):
            if i > 0: draw += " -- "
            draw += '(%f,%f)' % (self.points[i][0]*scale,self.points[i][1]*scale)
        draw += ' -- cycle;'
        tex.extend([draw])
        tex.extend([r'\node at (%f,%f) {%s};' % (1*scale,3.5*scale,label)])
        tex.extend([r'\end{scope}'])
        return tex

