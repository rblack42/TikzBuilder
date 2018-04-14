import json
import sys
from .parts.ALU import ALU

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
            for p in range(len(self.json)):
                data = self.json[p]
                part = data["part"]
                if part == "ALU":
                    alu = ALU(data)
                    tex.extend(alu.draw())
        self.tikz.extend(tex)

