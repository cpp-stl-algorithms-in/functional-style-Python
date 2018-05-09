import std

EVEN_NUMBERS = (0, 2, -1010, -64, 12)


def is_even(n):
    return n % 2 == 0


def test_all_of_empty_are_even():
    assert std.all_of((), is_even)


def test_all_of_even_numbers_are_even():
    assert std.all_of(EVEN_NUMBERS, is_even)
