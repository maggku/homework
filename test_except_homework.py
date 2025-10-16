from except_homework import division2

def test_division2():
    assert division2(10,2) == 5
    assert division2(10, 0) == None
    assert division2(10, "dog") == None