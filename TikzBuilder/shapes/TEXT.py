class TEXT(object):

    def __init__(self):
        self.pin_d = { }
        self.label = "txt1"

    def draw(self,x,y,scale,color):
        np = 1
        sp = 'e'
        print("placing %s pin%d" %(self.label,np))
        self.pin_d["pin%d" % np] = (x,y,sp)
        label = "+1"
        draw = r"\node at (%f,%f) {%s};" % (x,y,label)
        return [draw], self.pin_d

