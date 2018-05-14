def all_of(iterable, predicate):
    return all(map(predicate, iterable))


def any_of(iterable, predicate):
    return any(map(predicate, iterable))


def none_of(iterable, predicate):
    return not any_of(iterable, predicate)
