from src.math_operations import sum,subtract

def test_add():
    assert sum(2,3) == 5
    assert sum(-1,1)== 0
    assert sum(0,0) == 0    

def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(0,0) == 0
    assert subtract(-1,-1) == 0