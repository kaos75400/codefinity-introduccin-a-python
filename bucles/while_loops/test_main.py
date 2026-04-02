import pytest

from main import countdown


class TestCountdownBasic:
    def test_from_five(self):
        assert countdown(5) == [5, 4, 3, 2, 1]

    def test_from_one(self):
        assert countdown(1) == [1]

    def test_from_zero(self):
        assert countdown(0) == []

    def test_from_negative(self):
        assert countdown(-3) == []

    def test_is_descending(self):
        result = countdown(10)
        assert result == list(range(10, 0, -1))

    def test_length_matches_input(self):
        for n in range(1, 20):
            assert len(countdown(n)) == n

    def test_first_element_equals_start(self):
        assert countdown(7)[0] == 7

    def test_last_element_is_one(self):
        assert countdown(7)[-1] == 1


class TestCountdownValidation:
    def test_rejects_float(self):
        with pytest.raises(TypeError, match="entero"):
            countdown(5.5)

    def test_rejects_string(self):
        with pytest.raises(TypeError, match="entero"):
            countdown("5")

    def test_rejects_none(self):
        with pytest.raises(TypeError, match="entero"):
            countdown(None)

    def test_rejects_list(self):
        with pytest.raises(TypeError, match="entero"):
            countdown([5])
