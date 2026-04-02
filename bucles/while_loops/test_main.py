from main import countdown


def test_countdown_from_five():
    assert countdown(5) == [5, 4, 3, 2, 1]


def test_countdown_from_one():
    assert countdown(1) == [1]


def test_countdown_from_zero():
    assert countdown(0) == []


def test_countdown_from_negative():
    assert countdown(-3) == []


def test_countdown_result_is_descending():
    result = countdown(10)
    assert result == list(range(10, 0, -1))


def test_countdown_length():
    for n in range(1, 20):
        assert len(countdown(n)) == n
