from typing import Any, Dict, Tuple, List

class Graph:
    """Directed graph with adjacencies as neighbor→cost dicts for O(1) updates."""

    def __init__(self):
        # Each node maps to a dict: neighbor → (time, toll, scenic)
        self._adj: Dict[Any, Dict[Any, Tuple[float, float, float]]] = {}

    def add_node(self, node: Any) -> None:
        """Ensure a node exists."""
        self._adj.setdefault(node, {})

    def add_edge(self, u: Any, v: Any, cost: Tuple[float, float, float]) -> None:
        """Add or update a directed edge u → v in O(1)."""
        if not (isinstance(cost, tuple) and len(cost) == 3):
            raise ValueError("Cost must be a tuple of three floats")
        self.add_node(u)
        self.add_node(v)
        self._adj[u][v] = cost

    def remove_node(self, node: Any) -> None:
        """Remove a node and all incoming/outgoing edges."""
        if node not in self._adj:
            raise KeyError(f"Node {node} not found")
        # Remove outgoing
        del self._adj[node]
        # Remove any incoming edges
        for nbrs in self._adj.values():
            nbrs.pop(node, None)

    def remove_edge(self, u: Any, v: Any) -> None:
        """Remove edge u → v in O(1)."""
        try:
            del self._adj[u][v]
        except KeyError:
            raise ValueError(f"Edge {u} -> {v} not found")

    def neighbors(self, node: Any) -> List[Tuple[Any, Tuple[float, float, float]]]:
        """List (neighbor, cost) for a node."""
        if node not in self._adj:
            raise KeyError(f"Node {node} not found")
        return list(self._adj[node].items())

    def bfs(self, start: Any) -> List[Any]:
        """Breadth‑first traversal (unchanged)."""
        from collections import deque
        if start not in self._adj:
            raise KeyError(f"Node {start} not found")
        visited, order = {start}, []
        q = deque([start])
        while q:
            u = q.popleft()
            order.append(u)
            for v in self._adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return order

    def dfs(self, start: Any) -> List[Any]:
        """Depth‑first traversal (unchanged)."""
        if start not in self._adj:
            raise KeyError(f"Node {start} not found")
        visited, order = set(), []
        def _rec(u):
            visited.add(u)
            order.append(u)
            for v in self._adj[u]:
                if v not in visited:
                    _rec(v)
        _rec(start)
        return order
