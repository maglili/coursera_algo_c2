graph = {}

with open("./SCC.txt") as fh:
    for row in fh:
        node1, node2 = row.split()
        if node1 not in graph:
            graph[node1] = [node2]
        else:
            graph[node1].append(node2)
