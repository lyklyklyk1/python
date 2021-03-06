import sys


def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    for item in the_list:
        if(isinstance(item, list)):
            print_lol(item, indent, level+1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end="", file=fn)
            print(item, file=fn)
