def read_graph_file(filename):
    with open(filename, 'r') as file:
        content = file.read().splitlines()
    number_of_vertices = int(content[0])
    edges = [tuple(int(edge) for edge in line.split(' ')) for line in content[1:]]
    return number_of_vertices, edges
