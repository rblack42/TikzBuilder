from TikzBuilder.Builder import Builder
tb = Builder()

def test_page_head():
    assert r"\usepackage{circuitikz}" in tb.get_head()

def test_page_foot():
    assert r"\end{document}" in tb.get_foot()

def test_page_image():
    assert tb.get_image() == []

def test_dummy_page():
    tb = Builder('examples/demo.json')
    tb.load()
    data = tb.get_json()
    assert data[0]["part"] == "ALU"

def test_page():
    tb.run()
    tex = tb.get_tex()
    assert r"\begin{document}" in tex
    assert r"\end{document}" in tex
