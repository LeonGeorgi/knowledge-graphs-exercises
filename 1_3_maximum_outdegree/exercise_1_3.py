import sys
from collections import Counter

from util import read_graph_file


def exercise_1_3():
    filename = sys.argv[1]
    _, edges = read_graph_file(filename)

    vertex_out_degree = Counter(source for source, target in edges)
    max_out_degree = vertex_out_degree.most_common(1)[0][1]
    print('Maximum out-degree:', max_out_degree)

    vertices_with_max_out_degree = {vertex for vertex, count in vertex_out_degree.items() if count == max_out_degree}
    print('Vertices with maximum out-degree:', sorted(vertices_with_max_out_degree))


if __name__ == '__main__':
    exercise_1_3()
