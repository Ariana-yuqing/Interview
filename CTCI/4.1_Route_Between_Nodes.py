"""
    Given a directed graph, find out whether there is a route between two nodes
    A -> B
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C

    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
"""
from collections import deque


#  DFS
def find_route(g, start, end, route=None):
    """
        :type g: graph
        :type start : string
        :type end : string
        :type route: list
    """
    if route is None:
        route = []
    # The 'path' argument is not modified: the assignment "path = path + [start]" creates a new list.
    route = route + [start]
    if start == end:
        return route
    if start not in g:
        return None
    for k in g[start]:
        if k not in route:
            new_route = find_route(g, k, end, route)
            if new_route:
                return new_route
    return None


# BFS
def find_route_2(g, start, end):
    q = deque()
    q.append(start)
    predecessor = {}
    visited = []

    while q:
        cur = q.popleft()
        visited.append(cur)
        if cur == end:
            s = end
            route = []
            while s != start:
                route.append(s)
                s = predecessor[s]
            route.append(start)
            route.reverse()
            return route
        for k in g[cur]:
            if k not in visited:
                predecessor[k] = cur
                q.append(k)
    return None


def main():
    graph = {'A': ['E', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['G']}
    print(find_route(graph, 'A', 'D'))
    print(find_route_2(graph, 'A', 'D'))

if __name__ == '__main__':
    main()




