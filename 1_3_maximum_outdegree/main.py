import sys
from collections import Counter


def main():
    filename = sys.argv[1]
    _, edges = read_graph_file(filename)

    vertex_out_degree = Counter(source for source, target in edges)
    max_out_degree = vertex_out_degree.most_common(1)[0][1]
    print('Maximum out-degree:', max_out_degree)

    vertices_with_max_out_degree = {vertex for vertex, count in vertex_out_degree.items() if count == max_out_degree}
    print('Vertices with maximum out-degree:', sorted(vertices_with_max_out_degree))


def read_graph_file(filename):
    with open(filename, 'r') as file:
        content = file.read().splitlines()
    number_of_vertices = int(content[0])
    edges = [tuple(int(edge) for edge in line.split(' ')) for line in content[1:]]
    return number_of_vertices, edges


if __name__ == '__main__':
    main()
