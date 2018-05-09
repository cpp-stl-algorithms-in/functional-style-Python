import std

EVEN_NUMBERS = (0, 2, -1010, -64, 12)
MIXED_NUMBERS = (0, 2, -1010, -64, 12, -3)


def is_even(n):
    return n % 2 == 0


def test_all_of_with_empty_set_returns_true():
    assert std.all_of((), is_even) is True


def test_all_of_with_all_elements_fulfilling_predicate_returns_true():
    assert std.all_of(EVEN_NUMBERS, is_even) is True


def test_all_of_with_some_elements_not_fulfilling_predicate_returns_false():
    assert std.all_of(MIXED_NUMBERS, is_even) is False
