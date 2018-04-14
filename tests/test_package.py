from TikzBuilder.Builder import Builder

def test_package():
    tb = Builder()
    assert "version" in tb.version()

