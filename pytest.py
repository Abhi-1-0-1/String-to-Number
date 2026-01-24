import pytest
from converter import convert

class TestBasicConversions:
    def test_single_digits(self):
        assert convert("zero") == 0
        assert convert("five") == 5
        assert convert("nine") == 9

    def test_teens_and_tens(self):
        assert convert("thirteen") == 13
        assert convert("forty") == 40
        assert convert("ninety nine") == 99

    def test_hundreds(self):
        assert convert("one hundred") == 100
        assert convert("eight hundred seventy two") == 872

class TestComplexNumbers:
    def test_large_scales(self):
        assert convert("one thousand") == 1000
        assert convert("one million two hundred thousand five hundred") == 1200500
        assert convert("five billion") == 5000000000

    def test_negative_numbers(self):
        assert convert("minus fifty") == -50
        assert convert("minus one million") == -1000000

    def test_with_and_conjunction(self):
        # Testing that "and" is successfully ignored
        assert convert("one hundred and twenty five") == 125
        assert convert("two thousand and one") == 2001

class TestErrorHandling:
    def test_empty_string(self):
        with pytest.raises(ValueError, match="The input string is empty"):
            convert("")

    def test_invalid_words(self):
        with pytest.raises(KeyError, match="not recognized"):
            convert("one hundred pizza")

    def test_malformed_minus(self):
        with pytest.raises(ValueError, match="must be followed by a number"):
            convert("minus")