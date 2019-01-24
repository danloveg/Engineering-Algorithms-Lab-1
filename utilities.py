def str_to_int(string):
    try:
        return int(string)
    except ValueError:
        raise ValueError('Value "{}" could not be converted to an integer'.format(string))

def close_app():
    print ('Exiting.')