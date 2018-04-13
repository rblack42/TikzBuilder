# test the testing system

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case("something") == 'Something'
