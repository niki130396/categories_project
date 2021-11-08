

def bfs(graph, source, destination):
    queue = [(source, [source])]
    while queue:
        vertex, path = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == destination:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest(graph, source, destination):
    try:
        return next(bfs(graph, source, destination))
    except StopIteration:
        return None


graph = {'A': set(['B', 'D']),
         'B': set(['C', 'D']),
         'C': set([]),
         'D': set([])
         }

print(shortest(graph, 'A', 'C'))
