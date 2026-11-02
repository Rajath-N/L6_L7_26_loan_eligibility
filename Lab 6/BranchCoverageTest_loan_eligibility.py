import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


# CREDIT BAND TEST CASES

def test_excellent_band():
    assert credit_band(800) == "excellent"


def test_good_band():
    assert credit_band(700) == "good"


def test_fair_band():
    assert credit_band(600) == "fair"


def test_poor_band():
    assert credit_band(500) == "poor"


def test_minimum_valid_score():
    assert credit_band(300) == "poor"


def test_maximum_valid_score():
    assert credit_band(900) == "excellent"


def test_invalid_low_score():
    with pytest.raises(ValueError):
        credit_band(200)


def test_invalid_high_score():
    with pytest.raises(ValueError):
        credit_band(950)


# LOAN ELIGIBILITY TEST CASES

def test_eligible():
    assert is_eligible(30, 50000, "salaried", 800) is True


def test_unknown_employment():
    with pytest.raises(ValueError):
        is_eligible(30, 50000, "unemployed", 800)


def test_age_below_limit():
    assert is_eligible(20, 50000, "salaried", 800) is False


def test_age_above_limit():
    assert is_eligible(61, 50000, "salaried", 800) is False


def test_income_below_salaried_minimum():
    assert is_eligible(30, 20000, "salaried", 800) is False


def test_income_below_self_employed_minimum():
    assert is_eligible(30, 30000, "self_employed", 800) is False


def test_poor_credit_not_eligible():
    assert is_eligible(30, 50000, "salaried", 500) is False


def test_self_employed_eligible():
    assert is_eligible(30, 50000, "self_employed", 700) is True


def test_minimum_age_eligible():
    assert is_eligible(21, 50000, "salaried", 800) is True


def test_maximum_age_eligible():
    assert is_eligible(60, 50000, "salaried", 800) is True


# INTEREST RATE TEST CASES

def test_excellent_interest_rate():
    assert interest_rate(800, "salaried", False) == 8


def test_good_interest_rate():
    assert interest_rate(700, "salaried", False) == 10


def test_fair_interest_rate():
    assert interest_rate(600, "salaried", False) == 13


def test_self_employed_interest_rate():
    assert interest_rate(800, "self_employed", False) == 9


def test_collateral_interest_rate():
    assert interest_rate(800, "salaried", True) == 6


def test_self_employed_with_collateral():
    assert interest_rate(800, "self_employed", True) == 7


def test_poor_credit_interest_rate():
    assert interest_rate(500, "salaried", False) == 13