import std


def is_even(n):
    return n % 2 == 0


def test_all_of_empty_are_even():
    assert std.all_of((), is_even)
