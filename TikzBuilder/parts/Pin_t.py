class Pin_t(object):

    points = [
        (0,0),
        (0.25,0),
        (0.25,0.5),
        (0,0.5)
    ]
    
    def draw(self, x, y, shift, label):
        x = x - 0.125
        y = y - 0.25
        dy = 0
        tex = []
        draw = r'\begin{scope}[shift={(%f,%f)}]' % (x,y)
        draw += r"\draw [fill=blue!30] "
        for i in range (len(self.points)):
            if i > 0: draw += " -- "
            draw += '(%f,%f)' % (self.points[i][0],self.points[i][1])
        draw += ' -- cycle;'
        tex.append(draw)
        yl = 0
        if shift == 's': yl = 0.125
        if shift == 'n': yl = 0.375
        tex += [r'\node at (0.125,%f) {\tiny{%d}};' % (yl,label)]
        tex += ['\end{scope}']
        return tex
    
