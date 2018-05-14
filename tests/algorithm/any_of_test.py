import std

EVEN_NUMBERS = (0, 2, -1010, -64, 12)
MIXED_NUMBERS = (0, 2, -1010, -64, 12, -3)


def is_odd(n):
    return n % 2 != 0


def test_any_of_with_empty_set_returns_false():
    assert std.any_of((), is_odd) is False


def test_any_of_with_some_elements_fulfilling_predicate_returns_true():
    assert std.any_of(MIXED_NUMBERS, is_odd) is True


def test_any_of_with_no_elements_fulfilling_predicate_returns_False():
    assert std.any_of(EVEN_NUMBERS, is_odd) is False
