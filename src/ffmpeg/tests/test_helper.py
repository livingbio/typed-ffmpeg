from ..helper import calculate_dynamic_types


def test_calculate_dynamic_types() -> None:
    fn = "['audio'] + ['video'] if response else []"
    assert calculate_dynamic_types(fn, response=True) == ["audio", "video"]
    assert calculate_dynamic_types(fn, response=False) == ["audio"]
