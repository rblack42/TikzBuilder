from TikzBuilder import TikzBuilder

def test_package():
    tb = TikzBuilder()
    assert "version" in tb.version()

