class GraphNode:

    def __init__(self, value):
        self._value = value
        self._to = set()

    # make n a direct destination for self
    def to(self, n):
        self._to.add(n)

    # traveser generator based on dfs/bfs specification :-)
    def __find_reachable(self, dfs=True):
        def traverse():
            toOpen, toReturn = list(self._to), []
            if dfs:
                def _add(q, to):
                    q.append(to)
            else:
                def _add(q, to):
                    q.insert(0, to)

            while len(toOpen) > 0:
                top = toOpen.pop(0)
                toReturn.append(top)
                for to in top._to:
                    # O(N) check. Use a set to make it O(1)
                    if to not in toReturn:
                        _add(toOpen, to)

            return toReturn
        return traverse

    # return list of all reachable nodes from self via bfs
    # nearer nodes appear earlier in returned list
    def bfs(self):
        return self.__find_reachable(True)()

    # return list of all reachable nodes from self via dfs
    def dfs(self):
        return self.__find_reachable(False)()
