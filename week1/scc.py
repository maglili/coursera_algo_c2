import gc
import sys, threading


def reversed_arc(graph):
    graph_rev = {}
    for tail_node, head_node_list in graph.items():
        for node in head_node_list:
            if node not in graph_rev:
                graph_rev[node] = [tail_node]
            else:
                graph_rev[node].append(tail_node)
    return graph_rev


def DFS(graph, node):

    global t

    explored[node] = True

    # check if a sink node
    if node in graph:
        for head_node in graph[node]:
            if head_node not in explored:
                # print("find", head_node, "---")
                DFS(graph, head_node)
    t += 1
    magic_order[node] = t


def DFS_Loop(graph, info=False):
    global t, explored, magic_order
    t = 0
    last_t = 0
    explored = {}
    magic_order = {}
    num_graph = 0

    scc_info = [0] * 5

    # reverse dict key
    graph_key = list(graph.keys())
    graph_key.sort(reverse=True)

    for node in graph_key:
        if node not in explored:
            # print("node:", node, "=====")
            DFS(graph, node)
            scc_info.sort()
            if info:
                for idx, num in enumerate(scc_info):
                    if (t - last_t) > num:
                        scc_info[idx] = t - last_t
                        break
            last_t = t

    return scc_info


def mapping_magic_order(graph):
    new_graph = {}

    for tail_node, head_node_list in graph.items():

        new_node = magic_order[tail_node]
        new_head_node_list = []

        for i in head_node_list:
            new_head_node_list.append(magic_order[i])

        new_graph[new_node] = new_head_node_list

    return new_graph


def kosaraju_scc(graph):
    global new_graph, grev
    scc_info = []

    # reversed graph
    grev = reversed_arc(graph)

    # 1st DFS on reversed graph
    DFS_Loop(grev)
    # print(magic_order)
    print("\n===1st DFS finish!===\n")

    del grev
    gc.collect()

    # map magic_order on graph
    new_graph = mapping_magic_order(graph)
    print("\n===map magic_order finish!===\n")

    del graph
    gc.collect()

    # 2st DFS on reversed graph
    scc_info = DFS_Loop(new_graph, info=True)

    # output answer
    scc_info.sort(reverse=True)

    return scc_info


def open_data(input_path):

    graph = {}

    with open(input_path) as fh:
        for row in fh:
            elements = row.split()
            if elements == []:
                continue
            node1, node2 = elements
            node1, node2 = int(node1), int(node2)
            if node1 not in graph:
                graph[node1] = [node2]
            else:
                graph[node1].append(node2)

            # sink node
            if node2 not in graph:
                graph[node2] = []

    return graph


def main():
    graph = open_data("./SCC.txt")
    scc_info = kosaraju_scc(graph)
    print(scc_info)


if __name__ == "__main__":
    """
    threading idea: https://www.coursera.org/learn/algorithms-graphs-data-structures/discussions/weeks/1/threads/gvQvXVCGEee3RwoqcUym2A
    """
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()
