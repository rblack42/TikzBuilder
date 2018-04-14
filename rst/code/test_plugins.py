import sys
import traceback

from shapes import *

datatype = 'ALU'

class Builder(object):

    def draw_shape(self, shape, name):
        try:
            handler = getattr(sys.modules['shapes.%s' % shape], shape)
            obj = handler()
            tex = obj.draw(name)
        except:
            traceback.print_exc()
            tex = ['no handler found']
        return tex

if __name__ == '__main__':
    shape = sys.argv[1]
    name = sys.argv[2]
    b = Builder()
    tex = b.draw_shape(shape,name)
    print(tex)
