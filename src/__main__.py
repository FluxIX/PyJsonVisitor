# Cannot use a relative import here.
from json_visitor.main import main as entry_point

if __name__ == '__main__':
    import sys
    ret_value = entry_point( sys.argv[ 1: ] )

    sys.exit( ret_value )
