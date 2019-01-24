import graphtools
import grouping_algorithm as al
import plac
import atexit
import utilities as util
from pathlib import Path

def main(filename: "Path to file containing adjacency matrix"):
    try:
        filepath = Path(filename)

        if filepath.is_file(): 
            graph = graphtools.convert_text_matrix_to_graph(filepath)
            al.split_into_groups(graph, len(graph))
        else:
            print('"{}" does not exist.'.format(filename))

    except Exception as e:
        print(e)

if __name__ == '__main__':
    atexit.register(util.close_app)
    plac.call(main)
