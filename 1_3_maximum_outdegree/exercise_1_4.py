import itertools
import sys

from util import read_graph_file


def main():
    filename = sys.argv[1]
    number_of_vertices, edges = read_graph_file(filename)
    print(number_of_vertices, len(edges))
    for index, grouped_edges in itertools.groupby(sorted(edges), key=lambda x: x[0]):
        grouped_edges = list(grouped_edges)
        outgoing_edge = grouped_edges[0][0]
        print(outgoing_edge, " ".join(str(target) for source, target in grouped_edges))


if __name__ == '__main__':
    main()
