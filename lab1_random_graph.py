import graphtools
import grouping_algorithm as al
import plac
import atexit
import utilities as util

def main(size: "Size of graph", sparseness: "Percentage of graph that is sparse"):
    size_num = util.str_to_int(size)

    graph = graphtools.create_symmetric_graph(size_num, util.str_to_int(sparseness))
    al.split_into_groups(graph, size_num)

if __name__ == '__main__':
    atexit.register(util.close_app)
    plac.call(main)
