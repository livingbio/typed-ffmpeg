from typing import Any, Literal  # noqa: F401


class FilterNode:
    def __init__(self, stream: "Stream", name: str, **kwargs: Any) -> None:
        ...

    def stream(self) -> "Stream":
        raise NotImplementedError()


class Stream:
    def acompressor(
        self,
        level_in: float = 1.0,
        mode: Literal["upward", "downward"] = "downward",
        threshold: float = 0.125,
        ratio: float = 2,
        attack: float = 20,
        release: float = 250,
        makeup: float = 1,
        knee: float = 2.82843,
        link: Literal["average", "maximum"] = "average",
        detection: Literal["peak", "rms"] = "rms",
        mix: float = 1,
    ) -> "Stream":
        return FilterNode(
            self,
            "acompressor",
            level_in=level_in,
            mode=mode,
            threshold=threshold,
            ratio=ratio,
            attack=attack,
            release=release,
            makeup=makeup,
            knee=knee,
            link=link,
            detection=detection,
            mix=mix,
        ).stream()
