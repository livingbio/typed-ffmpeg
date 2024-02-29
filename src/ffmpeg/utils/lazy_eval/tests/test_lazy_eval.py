from __future__ import annotations

from json import loads
from typing import Generator

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ....dag.serialize import dumps
from ..schema import PlaceHolder


@pytest.fixture
def VarX() -> Generator[PlaceHolder, None, None]:
    yield PlaceHolder(key="X")


@pytest.fixture
def VarY() -> Generator[PlaceHolder, None, None]:
    yield PlaceHolder(key="Y")


def test_lazyoperator_number(snapshot: SnapshotAssertion, VarX: PlaceHolder, VarY: PlaceHolder) -> None:
    Op = ((1 + VarX + VarY - 5) * 3) / 4**2 * (-VarX) + (+VarY) + (abs(VarX)) + (VarX % VarY) + (VarX // VarY)

    assert snapshot(name="repr") == str(Op)
    assert snapshot(extension_class=JSONSnapshotExtension) == loads(dumps(Op))
    assert snapshot() == Op.keys()

    with pytest.raises(KeyError):
        Op.eval()

    with pytest.raises(KeyError):
        Op.eval(**{VarX.key: 30})

    assert snapshot == Op.eval(**{VarX.key: 30, VarY.key: 45})
    assert snapshot == Op
