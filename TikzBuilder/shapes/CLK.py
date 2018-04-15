
def CLK(w):
    draw = r"\draw [black]"
    draw += "(%f,0)" % (0.5*w-0.125)
    draw += " -- "
    draw += "(%f,%f)" % (0.5*w,0.125)
    draw += " -- "
    draw += "(%f,0);" % (0.5*w+0.125)
    return draw

