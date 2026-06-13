def test_passing():
    assert (123) == (123)
    
def test_one_in_list():
    assert 1 in [1,2,3]
    
def test_a_lt_b():
    assert 'a' < 'b'
    
def test_rondi():
    assert 'rondi' not in 'rondinelle'