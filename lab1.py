import graphtools
import plac

def main(size: "Size of graph", sparseness: "Percentage of graph that is sparse"):
    try:
        graph = graphtools.create_symmetric_graph(strtoint(size), strtoint(sparseness))
        print(graph)

    except Exception as e:
        print(e)

def strtoint(string):
    try:
        return int(string)
    except ValueError:
        raise ValueError('Value "{}" could not be converted to an integer'.format(string))

if __name__ == '__main__':
    plac.call(main)
