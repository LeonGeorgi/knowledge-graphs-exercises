import sys
from collections import Counter

from util import read_graph_file


def exercise_1_3():
    filename = sys.argv[1]
    number_of_vertices, edges = read_graph_file(filename)

    vertex_degrees = []
    for vertex in range(number_of_vertices):
        vertex_degrees.append(len(list(edge for edge in edges if edge[0] == vertex)))
    max_out_degree = max(vertex_degrees)
    print('Maximum out-degree:', max_out_degree)

    vertices_with_max_out_degree = [vertex for vertex, degree in enumerate(vertex_degrees) if degree == max_out_degree]
    print('Vertices with maximum out-degree:', sorted(vertices_with_max_out_degree))


if __name__ == '__main__':
    exercise_1_3()
