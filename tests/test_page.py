from TikzBuilder import TikzBuilder
tb = TikzBuilder()

def test_page_head():
    assert r"\usepackage{tikz}" in tb.page_head()

def test_page_foot():
    assert r"\end{document}" in tb.page_foot()

def test_page_image():
    assert tb.page_image() == []

def test_dummy_page():
    tb = TikzBuilder('examples/demo.json')
    tb.load()
    data = tb.page_json()
    assert data[0]["part"] == "ALU"

