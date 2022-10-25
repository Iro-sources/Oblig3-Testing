from years import checkLeapYear

def test_is_divisible_by_4():
    assert checkLeapYear(4) == True

def test_is_divisible_by_100():
    assert checkLeapYear(100) == False

def test_is_divisible_by_400():
    assert checkLeapYear(400) == True

def test_is_divisible_by_200():
    assert checkLeapYear(200) == True


