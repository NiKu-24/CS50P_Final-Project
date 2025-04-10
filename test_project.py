import pytest
import project

# Converters
def test_convert_to_binary():
    assert project.convert_to_binary(0) == "0"
    assert project.convert_to_binary(2) == "10"
    assert project.convert_to_binary("2") == "10"
    assert project.convert_to_binary(" 5 ") == "101"
    
def test_convert_to_binary_invalid():
    with pytest.raises(ValueError):
        project.convert_to_binary("abc")
        
    with pytest.raises(ValueError):
        project.convert_to_binary("-5")
        
    with pytest.raises(ValueError):
        project.convert_to_binary("")    
        
def test_convert_to_decimal():
    assert project.convert_to_decimal("0") == 0
    assert project.convert_to_decimal("1") == 1
    assert project.convert_to_decimal("10") == 2
    assert project.convert_to_decimal(" 11 ") == 3
    
def test_convert_to_decimal_invalid():
    with pytest.raises(ValueError):
        project.convert_to_decimal("abc")
        
    with pytest.raises(ValueError):
        project.convert_to_decimal("102")
        
    with pytest.raises(ValueError):
        project.convert_to_decimal("")
    with pytest.raises(ValueError):
        project.convert_to_decimal("1 0")
        
# Calculations
def test_add_binary():
    assert project.add_binary("0", "0") == "0"
    assert project.add_binary("10", "1") == "11"
    assert project.add_binary("10", "10") == "100"
    assert project.add_binary(" 100", " 10 ") == "110"
    
def test_add_binary_invalid():
    with pytest.raises(ValueError):
        project.add_binary("abc", "10")
        
    with pytest.raises(ValueError):
        project.add_binary("10a", "abc")
    
    with pytest.raises(ValueError):
        project.add_binary("10@", "10£")

    with pytest.raises(ValueError):
        project.add_binary("", "10")  

    with pytest.raises(ValueError):
        project.add_binary("1001", "")  
    
    with pytest.raises(ValueError):
        project.add_binary("10 1", "10")
        
def test_subtract_binary():
    assert project.subtract_binary("0", "0") == "0"
    assert project.subtract_binary("10", "1") == "1"
    assert project.subtract_binary("10", "10") == "0"
    assert project.subtract_binary(" 100", " 10 ") == "10"
    
def test_subtract_binary_invalid():    
    with pytest.raises(ValueError):
        project.subtract_binary("abc", "10")
        
    with pytest.raises(ValueError):
        project.subtract_binary("10a", "abc")
    
    with pytest.raises(ValueError):
        project.subtract_binary("10@", "10£")

    with pytest.raises(ValueError):
        project.subtract_binary("", "10")  

    with pytest.raises(ValueError):
        project.subtract_binary("1001", "")  
    
    with pytest.raises(ValueError):
        project.subtract_binary("10 1", "10")
        
    with pytest.raises(ValueError):
        project.subtract_binary("1", "10")
        
def test_multiply_binary():
    assert project.multiply_binary("0", "0") == "0"
    assert project.multiply_binary("10", "1") == "10"
    assert project.multiply_binary("10", "10") == "100"
    assert project.multiply_binary(" 100", " 10 ") == "1000"
    
def test_multiply_binary_invalid():    
    with pytest.raises(ValueError):
        project.multiply_binary("abc", "10")
        
    with pytest.raises(ValueError):
        project.multiply_binary("10a", "abc")
    
    with pytest.raises(ValueError):
        project.multiply_binary("10@", "10£")

    with pytest.raises(ValueError):
        project.multiply_binary("", "10")  

    with pytest.raises(ValueError):
        project.multiply_binary("1001", "")  
    
    with pytest.raises(ValueError):
        project.multiply_binary("10 1", "10")
        
def test_divide_binary():
    assert project.divide_binary("10", "1") == "10.0"           
    assert project.divide_binary("1011", "10") == "101.1"       
    assert project.divide_binary("11", "10") == "1.1"           
    assert project.divide_binary("1", "10") == "0.1"            
    assert project.divide_binary("0", "1") == "0.0"
    
def test_divide_binary_invalid():
    with pytest.raises(ValueError):
        project.divide_binary("abc", "10")
        
    with pytest.raises(ValueError):
        project.divide_binary("10", "1 0")
        
    with pytest.raises(ValueError):
        project.divide_binary("", "1")

    with pytest.raises(ValueError):
        project.divide_binary("101", "")
        
    assert project.divide_binary("101", "0") == "Error: You can't divide by zero."
    