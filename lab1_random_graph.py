import graphtools
import splitting_algorithm as al
import plac
import atexit
import utilities as util

def main(size: "Size of graph", sparseness: "Percentage of graph that is sparse"):
    try:
        graph = graphtools.create_symmetric_graph(util.str_to_int(size), util.str_to_int(sparseness))
        al.split_into_groups(graph, size)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    atexit.register(util.close_app)
    plac.call(main)
