import json
import sys

class TikzBuilder(object):

    HEAD = r"""
\documentclass{standalone}
\usepackage{tikz}
\usetikzpackage{circuitikz}
\begin{document}
\begin{tikzpicture}
"""

    FOOT = r"""
\end{tikzpicture}
\end{document}
"""

    def __init__(self,fname='examples/machine.json'):
        self.fname = fname
        self.head = self.HEAD.split()
        self.foot = self.FOOT.split()
        self.tikz = []
        self.json = []

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
        print(self.json)


    def version(self):
        return "version: 0.1.0.dev"

    def page_head(self):
        return self.head

    def page_foot(self):
        return self.foot

    def page_image(self):
        return self.tikz

    def page_json(self):
        return self.json

    def page_assemble(self):
        tex = []
        for l in self.head:
            tex.append(l)
        for l in self.tikz:
            tex.append(l)
        for l in self.foot:
            tex.append(l)
