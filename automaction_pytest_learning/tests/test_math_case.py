import pytest

products = [
    (3,2,6),
    (1,5,5),
    (3,0,0),
    (5,-1,-5),
    (-5,-8,40),
    (1.2, 5.1, 6.119999999999999)  
]

@pytest.mark.parametrize('a,b,product',products)
def test_mul_multi_varibles(a,b,product):
    print(a*b)

    assert a * b == product

