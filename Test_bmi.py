from lab2 import bmi as bmi
def test_bmi_normal_weight():
    result=bmi.calculate.bmi(1.73,60)
    assert(result==0)
    return "0"
def test_bmi_over_weight():
    result=bmi.calculate.bmi(1.73,60)
    assert(result==0)
    return "1"
def test_bmi_under_weight():
    
    result=bmi.calculate.bmi(1.73,60)
    assert(result==0)
    return "-1"