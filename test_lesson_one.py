import pytest
import lesson_one

def test_for_compare_two_numbers():
    assert lesson_one.compare_two_numbers(3,7) == 7
    assert lesson_one.compare_two_numbers(5,2) == 5
    assert lesson_one.compare_two_numbers(3,3) == 3

def test_for_check_year():
    assert lesson_one.check_year(2008) == "Yes"
    assert lesson_one.check_year(2007) == "No"
    assert lesson_one.check_year(2900) == "No"

def test_for_rook_attack():
    assert lesson_one.rook_attack("G5","B5") == "Yes"

def test_for_ice_cream():
    assert lesson_one.icecream(3) == "Yes"
    assert lesson_one.icecream(5) == "Yes"
    assert lesson_one.icecream(6) == "No"

def test_for_even_number():
    assert lesson_one.even_numbers(8,2) == [4, 6]
    assert 100 in lesson_one.even_numbers(4,122)
    assert 4 not in lesson_one.even_numbers(4,122)
    assert 122 not in lesson_one.even_numbers(4,122)