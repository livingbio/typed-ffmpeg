from __future__ import annotations

from collections import deque


def is_dag(graph: dict[str, set[str]]) -> bool:
    in_degree = {u: 0 for u in graph}  # Initialize in-degree of each node to 0

    # Calculate in-degree of each node
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in graph if in_degree[u] == 0])
    count = 0

    while queue:
        u = queue.popleft()
        count += 1

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return count == len(graph)
