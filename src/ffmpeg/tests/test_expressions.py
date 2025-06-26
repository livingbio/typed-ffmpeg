from .. import expressions


def test_expressions() -> None:
    assert expressions.if_(expressions.Expression("A") * "B", "C") == "if(A*B,C)"
