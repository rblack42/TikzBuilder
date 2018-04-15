import json
import sys
import traceback
from .shapes import *

class Builder(object):

    HEAD = r"""
\documentclass[preview]{standalone}
\usepackage{circuitikz}
\usetikzlibrary{shapes.geometric}
\begin{document}
\begin{tikzpicture}
"""

    FOOT = r"""
\end{tikzpicture}
\end{document}
"""
    def __init__(self,fname='examples/demo.json'):
        self.fname = fname
        self.head = self.HEAD.split()
        self.foot = self.FOOT.split()
        self.tikz = []
        self.json = []
        self.texfile = 'demo.tex'

    def load(self):
        try:
            with open(self.fname) as json_data:
                self.json = json.load(json_data)
        except:
            self.json = []

    def run(self):
        self.load()
        if self.json == []:
            print("Error opening data file:", self.fname)
            sys.exit()
        print("Building image from",self.fname)
        self.build()
        fout = open(self.texfile,'w')
        self.assemble()
        for l in self.tex:
            fout.write("%s\n" % l)
        fout.close()

    def version(self):
        return "version: 0.1.0.dev"

    def get_head(self):
        return self.head

    def get_foot(self):
        return self.foot

    def get_tex(self):
        return self.tex

    def get_image(self):
        return self.tikz

    def get_json(self):
        return self.json

    def assemble(self):
        tex = []
        for l in self.head:
            tex.append(l)
        for l in self.tikz:
            tex.append(l)
        for l in self.foot:
            tex.append(l)
        self.tex = tex

    def build(self):
        """process data file adding "parts"""
        tex = []
        if len(self.json) > 0:
            self.pin_data = {}
            for p in range(len(self.json)):
                data = self.json[p]
                shape = data["part"]
                if shape == "WIRE": continue
                label = data["label"]
                x = float(data["x"])
                y = float(data["y"])
                color = data["color"]
                scale = float(data["scale"])
                try:
                    cname = getattr(
                            sys.modules[
                                'TikzBuilder.shapes.%s' % shape
                            ],shape
                    )
                    handler = cname()
                    data,pin_d = handler.draw(x,y,scale,color)
                    self.pin_data[label] = pin_d
                    self.tikz.extend(data)
                except:
                    traceback.print_exc()

            # sweep over data handling wires
            for p in range(len(self.json)):
                data = self.json[p]
                shape = data["part"]
                if not shape == "WIRE": continue
                try:
                    cname = getattr(
                            sys.modules[
                                'TikzBuilder.shapes.%s' % shape
                            ], shape
                    )

                    handler = cname()
                    tex = handler.draw(data,self.pin_data)
                    self.tikz.extend(tex)
                except:
                    traceback.print_exc()



