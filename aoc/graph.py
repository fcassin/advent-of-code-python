import collections
import itertools

def _route_cost(route, distances):
    cost = 0
    length = len(route)

    for i in range(length):
        current = route[i]
        next = route[(i + 1) % length]

        cost = cost + distances[current][next]

    return cost

def _route_cost_no_return(route, distances):
    cost = 0
    length = len(route)

    for i in range(length):
        if i < length - 1:
            current = route[i]
            next = route[(i + 1) % length]

            cost = cost + distances[current][next]

    return cost

def travelling_salesman(vertices, edges, origin=None):
    """
    Travelling salesman is a classic algorithmic problem in the fields of computer 
    science and operations research.

    This implementation finds the shortest possible route that visits each vertex
    exactly once and returns to the starting vertex.

    vertices: List of vertex identifiers (e.g., city names)
    edges: List of tuples representing edges in the format (vertex1, vertex2, weight)
    origin: Optional starting vertex

    Example usage may be found in Advent of Code:
    - 2015, Day 9, Part 1
    """
    weights = collections.defaultdict(lambda: collections.defaultdict(int))

    for edge in edges:
        weights[edge[0]][edge[1]] = edge[2]
        weights[edge[1]][edge[0]] = edge[2]

    distances = [ [0] * len(vertices) for _ in range(len(vertices))]

    for i, start in enumerate(vertices):
        for j, stop in enumerate(vertices):
            if i == j:
                distances[i][j] = 0
                continue

            distances[i][j] = weights[start][stop]

    min_cost = float('inf')
    optimal_route = None
    permutations = itertools.permutations(range(len(vertices)))
    
    for permutation in permutations:
        cost = _route_cost(permutation, distances)

        if cost < min_cost:
            if origin is None or permutation[0] == origin:
                min_cost = cost
                optimal_route = permutation

    return min_cost, optimal_route

"""
Travelling salesman is a classic algorithmic problem in the fields of computer 
science and operations research.

This implementation finds the shortest possible route that visits each vertex
exactly once and does not return to the starting vertex.

vertices: List of vertex identifiers (e.g., city names)
edges: List of tuples representing edges in the format (vertex1, vertex2, weight)
origin: Optional starting vertex

Example usage may be found in Advent of Code:
- 2015, Day 9, Part 1
"""
def travelling_salesman_no_return(vertices, edges, origin=None):
    weights = collections.defaultdict(lambda: collections.defaultdict(int))

    for edge in edges:
        weights[edge[0]][edge[1]] = edge[2]
        weights[edge[1]][edge[0]] = edge[2]

    distances = [ [0] * len(vertices) for _ in range(len(vertices))]

    for i, start in enumerate(vertices):
        for j, stop in enumerate(vertices):
            if i == j:
                distances[i][j] = 0
                continue

            distances[i][j] = weights[start][stop]

    min_cost = float('inf')
    optimal_route = None
    permutations = itertools.permutations(range(len(vertices)))
    
    for permutation in permutations:
        cost = _route_cost_no_return(permutation, distances)

        if cost < min_cost:
            if origin is None or permutation[0] == origin:
                min_cost = cost
                optimal_route = permutation

    return min_cost, optimal_route

"""
Travelling showoff is similar to travelling salesman, but instead of minimizing the distance,
it maximizes it.

Example usage may be found in Advent of Code:
- 2015, Day 9, Part 2
"""
def travelling_showoff_no_return(vertices, edges):
    weights = collections.defaultdict(lambda: collections.defaultdict(int))

    for edge in edges:
        weights[edge[0]][edge[1]] = edge[2]
        weights[edge[1]][edge[0]] = edge[2]

    distances = [ [0] * len(vertices) for _ in range(len(vertices))]

    for i, start in enumerate(vertices):
        for j, stop in enumerate(vertices):
            if i == j:
                distances[i][j] = 0
                continue

            distances[i][j] = weights[start][stop]

    max_cost = 0
    optimal_route = None
    permutations = itertools.permutations(range(len(vertices)))
    
    for permutation in permutations:
        cost = _route_cost_no_return(permutation, distances)

        if cost > max_cost:
            max_cost = cost
            optimal_route = permutation

    return max_cost, optimal_route

"""
Breadth-First Search (BFS) algorithm implementation.

Explore the state space starting from 'start' state, using the provided
goal_func, hash_func, and neighbors_func to determine goal states,
state uniqueness, and neighboring states respectively.

Example usage may be found in Advent of Code:
- 2016, Day 11
"""
def bfs(start, goal_func, hash_func, neighbors_func):
    queue = collections.deque([(start, 0)])
    visited = set()
    
    while queue:
        current, depth = queue.popleft()
        
        state_hash = hash_func(current)
        if state_hash in visited:
            continue
        visited.add(state_hash)
        
        if goal_func(current):
            return depth
        
        for neighbor in neighbors_func(current):
            queue.append((neighbor, depth + 1))
    
    return -1