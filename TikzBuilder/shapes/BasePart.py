from .Pin import Pin
from .Pin_t import Pin_t

class BasePart(object):

    def __init__(self,data):
        """draw generic part""" 
        pass

    def draw(self):
        # get shape basic data
        x = self.x
        y = self.y
        h = self.h
        w = self.w
        yl = self.yl
        scale = self.scale
        label = self.label
        tex = []
        pin_d = {}
        # establish a scope for the shape
        tex.extend([r'\begin{scope}[shift={(%f,%f)}]' % (x,y)])

        # draw basic pins first
        pin = Pin()
        for p in range(len(self.pins)):
            xp = self.pins[p][0]*scale
            yp = self.pins[p][1]*scale
            sp = self.pins[p][2]
            np = p + 1
            print("placing %s pin%d" %(label,np))
            tex.extend(pin.draw(xp, yp, sp, np))
            pin_d["pin%d" % np] = (xp+x,yp+y,sp)

        # draw tall pins next
        pin = Pin_t()
        for p in range(len(self.pins_t)):
            xp = self.pins_t[p][0]*scale
            yp = self.pins_t[p][1]*scale
            sp = self.pins_t[p][2]
            np = len(self.pins) + p + 1
            print("placing %s pin%d" %(label,np))
            tex.extend(pin.draw(xp, yp, sp, np))
            pin_d["pin%d" % np] = (xp+x,yp+y,sp)

        # draw shape polygon next
        draw = ''
        draw += r"\draw [fill=%s!30]" % self.color
        for i in range (len(self.points)):
            if i > 0: draw += " -- "
            draw += '(%f,%f)' % \
                (self.points[i][0]*scale,self.points[i][1]*scale)
        draw += ' -- cycle;'
        tex.extend([draw])

        # place shape label
        tex.extend([r'\node at (%f,%f) {%s};' % (0.5*w*scale,yl*scale,label)])

# close scope
        tex.extend([r'\end{scope}'])
        return tex,pin_d

