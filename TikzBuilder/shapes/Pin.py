class Pin(object):

    points = [
        (0,0),
        (0.25,0),
        (0.25,0.25),
        (0,0.25)
    ]
    
    def draw(self, x, y, shift, label):
        x = x - 0.125
        y = y - 0.125
        dx = 0
        dy = 0
        if shift == 'w': dx = -0.125
        if shift == 'e': dx = 0.125
        if shift == 'n': dy = 0.125
        if shift == 's': dy = -0.125
        tex = []
        draw = r'\begin{scope}[shift={(%f,%f)}]' % (x+dx,y+dy)
        draw += r"\draw [fill=blue!30] "
        for i in range (len(self.points)):
            if i > 0: draw += " -- "
            draw += '(%f,%f)' % (self.points[i][0],self.points[i][1])
        draw += ' -- cycle;'
        tex.append(draw)
        tex.append(r'\node at (0.125,0.125) {\tiny{%d}};' % label)
        tex.append('\end{scope}')
        return tex
    
