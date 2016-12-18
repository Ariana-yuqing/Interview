"""
Leetcode 207. Course Schedule
First project is dependent on the second one
find a build order

e.g,. projects: a, b, c, d, e, f
      dependencies: (d, a) (b, f) (d, b) (a, f) (c, d)
"""
from collections import defaultdict


def build_order(projects, dependencies):
    """
    :param projects: list, list of all the projects
    :param dependencies: list,  list of pairs of dependencies
    :return: order: list, list of the build order
    """
    order = []
    # build the graph from [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]
    g = {}
    num_dep = defaultdict(int)
    for p, d in dependencies:
        num_dep[p] += 1
        if d in g:
            g[d].append(p)
        else:
            g[d] = [p]

    # put all the projects that do not require ant dependency to order list
    for p in projects:
        if num_dep[p] == 0:
            order.append(p)
            num_dep.pop(p)

    to_be_process = 0
    while to_be_process < len(order):
        cur = order[to_be_process]
        if cur in g:
            for v in g[cur]:
                num_dep[v] -= 1
                if num_dep[v] == 0:
                    order.append(v)
                    num_dep.pop(v)
            g.pop(cur)

        to_be_process += 1

    # check if all the projects are built
    for p in projects:
        if p not in order:
            return []
    return order


"""
Assume N projects and M dependencies
Build the graph: O(M) time and O(N) space
Find the start points: O(N) time
Queue: O(N) space
BFS, find the build order: O(M+N)

Overall: O(M+N) time and O(N) space
"""


# Topological sort via DFS
def build_order_DFS(projects, dependencies):
    """
    Arbitrarily select a node to do a DFS and put the node into order
      f            d-g
     /| \
    c |  b
     \| //\
      a / h
      |/
      e
    e.g.
    DFS(graph) => d g c b a e h
        DFS(b) => ... b a e h
            DFS(a) => ... a e
                DFS(e) => ... e
            DFS(h) => ... h
        DFS(f) => ... c
            DFS(c) => ... c
            DFS(a) X already visited
            DFS(b) X
        DFS(d) => ... d g
            DFS(g) => ... g
    """
    VISITING = 'VISITING'
    VISITED = 'VISITED'
    UNVISITED = 'UNVISITED'

    def doDFS(g, cur, order):
        if g[cur][0] == VISITING:
            return False
        if g[cur][0] == UNVISITED:
            g[cur][0] = VISITING
            for c in g[cur][1]:
                if not doDFS(g, c, order):
                    return False
            order.append(cur)
            g[cur][0] = VISITED
        return True

    # build the graph
    g = {}
    for p in projects:
        g[p] = [UNVISITED, []]
    for p, d in dependencies:
        g[d][1].append(p)

    order = []
    for p in projects:
        if g[p][0] == UNVISITED:
            # do a DFS
            if not doDFS(g, p, order):
                return []
    return list(reversed(order))


def main():
    dependencies = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    print(build_order(projects, dependencies))

    dependencies = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    print(build_order_DFS(projects, dependencies))

    dependencies = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
    projects = [0, 1, 2, 3, 4, 5, 6, 7]
    print(build_order_DFS(projects, dependencies))
    print(build_order(projects, dependencies))


if __name__ == '__main__':
    main()
