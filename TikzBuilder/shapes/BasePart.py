class BasePart(object):

    def __init__(self,data):
        self.x = 0
        if 'x' in data: self.x = data['x']
        self.y = 0
        if 'y' in data: self.y = data['y']
        self.w = 1
        if 'w' in data: self.w = data['w']
        self.h = 3
        if 'h' in data: self.h = data['h']
        self.label = "demo"
        if 'label' in data: self.label = data['label']

    def draw():
        pass

