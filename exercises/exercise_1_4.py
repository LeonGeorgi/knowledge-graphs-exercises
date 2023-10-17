import itertools
import sys

from util import read_graph_file


def main():
    filename = sys.argv[1]
    number_of_vertices, edges = read_graph_file(filename)
    print(number_of_vertices, len(edges))
    for vertex in range(number_of_vertices):
        outgoing_edges = [edge for edge in edges if edge[0] == vertex]
        print(vertex, " ".join(str(target) for source, target in outgoing_edges))


if __name__ == '__main__':
    main()
