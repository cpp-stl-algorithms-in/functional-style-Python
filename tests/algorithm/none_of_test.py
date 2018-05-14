import std

EVEN_NUMBERS = (0, 2, -1010, -64, 12)
MIXED_NUMBERS = (0, 2, -1010, -64, 12, -3)


def is_odd(n):
    return n % 2 != 0


def test_none_of_with_empty_set_returns_true():
    assert std.none_of((), is_odd) is True


def test_none_of_with_no_elements_fulfilling_predicate_returns_true():
    assert std.none_of(EVEN_NUMBERS, is_odd) is True


def test_none_of_with_some_elements_fulfilling_predicate_returns_false():
    assert std.none_of(MIXED_NUMBERS, is_odd) is False
