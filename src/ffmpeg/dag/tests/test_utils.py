import pytest

from ffmpeg.dag.utils import is_dag


@pytest.mark.parametrize(
    "graph, expected",
    [
        (
            {
                "A": set(),  # A has no incoming edges
                "B": {"A"},  # B has one incoming edge from A
                "C": {"A", "B"},  # C has incoming edges from A and B
                "D": {"C"},  # D has one incoming edge from C
            },
            True,
        ),
        (
            {
                # Simple Cycle
                "A": {"B"},
                "B": {"C"},
                "C": {"A"},  # Cycles back to A
            },
            False,
        ),
        (
            {
                # Self-loop
                "A": set(),
                "B": {"A", "B"},  # B has a self-loop
                "C": {"A"},
            },
            False,
        ),
        (
            {
                # Complex Cycle
                "A": {"B"},
                "B": {"C", "D"},
                "C": {"E"},
                "D": {"E"},
                "E": {"B"},  # Cycles back to B
                "F": {"A", "D"},
            },
            False,
        ),
        (
            {
                # Multiple Cycles
                "A": {"B"},
                "B": {"C", "D"},
                "C": {"A"},  # Cycles back to A
                "D": {"B"},  # Cycles back to B
                "E": {"F"},
                "F": {"E"},  # Cycles back to E
            },
            False,
        ),
        (
            # Linear Chain
            {
                "A": set(),
                "B": {"A"},  # B depends on A
                "C": {"B"},  # C depends on B
                "D": {"C"},  # D depends on C
            },
            True,
        ),
        (
            # Tree Structure
            {
                "A": set(),
                "B": {"A"},  # B depends on A
                "C": {"A"},  # C depends on A
                "D": {"B", "C"},  # D depends on B and C
                "E": {"C"},  # E depends on C
            },
            True,
        ),
        (
            # Complex Dependencies
            {
                "A": set(),
                "B": {"A"},  # B depends on A
                "C": {"A"},  # C depends on A
                "D": {"B"},  # D depends on B
                "E": {"B", "C"},  # E depends on B and C
                "F": {"D", "E"},  # F depends on D and E
                "G": {"F"},  # G depends on F
            },
            True,
        ),
        (
            # Disjoint Subgraphs
            {
                "A": set(),
                "B": {"A"},  # B depends on A
                "C": {"B"},  # C depends on B
                "D": set(),  # D is independent
                "E": {"D"},  # E depends on D
                "F": set(),  # F is independent
            },
            True,
        ),
        (
            #  Single Node
            {
                "A": set(),
            },
            True,
        ),
    ],
)
def test_is_dag(graph: dict[str, set[str]], expected: bool) -> None:
    assert is_dag(graph=graph) == expected, f"Expected {graph} to be {expected}"
