def all_of(iterable, predicate):
    return all(map(predicate, iterable))


def any_of(iterable, predicate):
    return any(map(predicate, iterable))
