from ..frozendict import FrozenDict, merge


def test_frozendict() -> None:
    d = FrozenDict({"a": 1, "b": 2})
    assert d["a"] == 1
    assert d["b"] == 2
    assert len(d) == 2
    assert d == {"a": 1, "b": 2}
    assert d != {"a": 1, "b": 3}
    assert d != {"a": 1, "b": 2, "c": 3}
    assert d != {"a": 1, "b": 2, "c": 3}

    assert dict(d) == {"a": 1, "b": 2}
    assert d | {} == {"a": 1, "b": 2}
    assert {} | d == {"a": 1, "b": 2}
    assert d | {"c": 3} == {"a": 1, "b": 2, "c": 3}
    assert {"c": 3} | d == {"c": 3, "a": 1, "b": 2}


def test_merge() -> None:
    assert isinstance(merge(), FrozenDict)
    assert merge() == {}
    assert merge({}) == {}
    assert merge(None) == {}
    assert merge({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
    assert merge({"a": 1}, {"b": 2}, {"c": 3}) == {"a": 1, "b": 2, "c": 3}
    assert merge({"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}) == {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
    }
    assert merge({"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}, {"e": 5}) == {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
    }
    assert merge({"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}, {"e": 5}, {"f": None}) == {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
    }
    assert merge({"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}, {"e": 5}, None) == {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
    }
    assert merge(
        {"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}, {"e": 5}, {"f": None}, {"g": None}
    ) == {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
