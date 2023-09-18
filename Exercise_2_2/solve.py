import networkx as nx
from sys import maxsize as infinite
from simple_queue import *


def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}  # Diccionario con la distancia desde
    # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    # ...

    open_list = Queue()
    closed_list = []

    open_list.enqueue(first_node)
    distance[first_node] = 0

    while not open_list.isEmpty():
        current_node = open_list.dequeue()
        closed_list.append(current_node)

        neighbors = [n for n in graph[current_node]]
        for neighbor in neighbors:
            if neighbor in closed_list:
                continue
            elif distance[neighbor] > distance[current_node] + 1:
                open_list.enqueue(neighbor)
                distance[neighbor] = distance[current_node] + 1

    return distance
