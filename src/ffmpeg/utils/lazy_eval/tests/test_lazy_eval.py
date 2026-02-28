from __future__ import annotations

from json import loads

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ....common.serialize import dumps
from ..schema import LazyOperator, Symbol

VarX = Symbol(key="X")

VarY = Symbol(key="Y")


@pytest.mark.parametrize(
    "oper",
    [
        VarX + 1,
        1 + VarX,
        VarX + VarY,
        VarX - 1,
        1 - VarX,
        VarX - VarY,
        VarX * 1,
        1 * VarX,
        VarX * VarY,
        VarX / 1,
        1 / VarX,
        VarX / VarY,
        VarX**1,
        1**VarX,
        VarX**VarY,
        -VarX,
        +VarX,
        abs(VarX),
        VarX % 1,
        1 % VarX,
        VarX % VarY,
        VarX // 1,
        1 // VarX,
        VarX // VarY,
    ],
)
def test_operator(snapshot: SnapshotAssertion, oper: LazyOperator) -> None:
    assert snapshot(name=str(oper), extension_class=JSONSnapshotExtension) == loads(
        dumps(oper)
    )
    assert snapshot(name=f"{oper}") == str(oper)

    assert snapshot(name=f"{oper}=") == oper.eval(**{VarX.key: 3, VarY.key: 5})


def test_lazyoperator_number(snapshot: SnapshotAssertion) -> None:
    Op = (
        ((1 + VarX + VarY - 5) * 3) / 4**2 * (-VarX)
        + (+VarY)
        + (abs(VarX))
        + (VarX % VarY)
        + (VarX // VarY)
    )

    assert snapshot(name="repr") == str(Op)
    assert snapshot(extension_class=JSONSnapshotExtension) == loads(dumps(Op))
    assert snapshot() == Op.keys()

    with pytest.raises(ValueError):
        Op.eval()

    with pytest.raises(ValueError):
        Op.eval(**{VarX.key: 30})

    assert snapshot(name="partial") == str(Op.partial(**{VarX.key: 30}))

    assert Op.ready() is False
    assert snapshot == Op.eval(**{VarX.key: 30, VarY.key: 45})
    assert snapshot == Op
