from ..cli import init_config, load_config
from ..schema import FFMpegFilterManuallyDefined


def test_init_config() -> None:
    init_config()


def test_load() -> None:
    assert isinstance(load_config("acrossover"), FFMpegFilterManuallyDefined)
