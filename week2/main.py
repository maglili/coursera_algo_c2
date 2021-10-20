import numpy as np


def Dijkstra(g: dict, s: int):
    """
    input:
        g (dict): graph
        s (int): source node
    """
    # Initialize
    X = {s: True}  # vertices processed so far
    A = [1000000 for x in range(len(g))]  # computed shortest path distances
    A[s - 1] = 0
    print("len of g:", len(g))
    print()

    # Main loop
    while len(X) < len(g):

        min_ = np.inf
        w_star = None
        v_star = None

        for v in X:
            for edge in g[v]:

                w, l_vw = tuple(edge.split(","))
                w, l_vw = int(w), int(l_vw)

                if w in X:
                    continue

                # greedy score
                gdy_score = A[v - 1] + l_vw
                if gdy_score < min_:
                    min_ = gdy_score
                    w_star = w
                    v_star = v

        X[w_star] = True
        A[w_star - 1] = min_

        # print(v_star, "->", w_star, "dis:", min_)

    return A, X


if __name__ == "__main__":

    # graph
    g = {}

    # add data to graph
    path = "./dijkstraData.txt"
    # path = "./testcase.txt"

    with open(path, "r") as f:
        for idx, row in enumerate(f):
            row = row.split()[1:]
            g[idx + 1] = row

    # Dijkstra's shortest-path algorithm
    A, X = Dijkstra(g, 1)

    # output answer
    target = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for num in target:
        print(A[num - 1], end=",")

    # target = [x for x in range(len(g))]
    # for num in target:
    #     print(A[num], end=",")
