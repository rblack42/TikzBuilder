class WIRE(object):

    def __init__(self):
        pass

    def draw(self,data,pin_data):
        self.pin_data = pin_data
        self.data = data
        source = data["source"]
        drives = data["drives"]
        ps,pins = source.split('.')
        pd,pind = drives.split('.')
        cs = pin_data[ps][pins]
        cd = pin_data[pd][pind]
        print(cs,cd)
        print(data)
        x1 = cs[0]
        y1 = cs[1]
        x2 = cd[0]
        y2 = cd[1]
        draw = r"\draw [ultra thick]"
        draw += "(%f,%f)" % (x1,y1)
        draw += " -- "
        draw += "(%f,%f);" % (x2,y2)
        return [draw]
