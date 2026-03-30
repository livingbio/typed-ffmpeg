/**
 * Utility functions for working with directed acyclic graphs (DAGs).
 */

/**
 * Determine if a graph is a directed acyclic graph using Kahn's algorithm.
 *
 * @param graph - Adjacency list: node -> set of nodes it points to
 * @returns true if the graph is a DAG (no cycles)
 */
export function isDAG(graph: Record<string, Set<string>>): boolean {
  const inDegree: Record<string, number> = {};

  // Initialize in-degree of each node to 0
  for (const u of Object.keys(graph)) {
    if (!(u in inDegree)) inDegree[u] = 0;
  }

  // Calculate in-degree of each node
  for (const u of Object.keys(graph)) {
    for (const v of graph[u]) {
      inDegree[v] = (inDegree[v] ?? 0) + 1;
    }
  }

  const queue: string[] = [];
  for (const u of Object.keys(graph)) {
    if (inDegree[u] === 0) queue.push(u);
  }

  let count = 0;
  while (queue.length > 0) {
    const u = queue.shift()!;
    count++;

    for (const v of graph[u]) {
      inDegree[v]--;
      if (inDegree[v] === 0) queue.push(v);
    }
  }

  return count === Object.keys(graph).length;
}
