from .python2latex import *

__all__ = ["dumps", "dump"]


def dumps(name, obj):
    """Convert a nested Python structure to a string accessible in LaTeX.

    Args:
        name (str): The name of the LaTeX variable to save the data to.
        obj (dict or list): The Python object to make accessible in LaTeX.

    Returns:
        str: A string of LaTeX code.
    """
    return python2latex(name, obj).dump()


def dump(name, obj, fp):
    """Convert a nested Python structure to a file accessible in LaTeX.

    Args:
        name (str): The name of the LaTeX variable to save the data to.
        obj (dict or list): The Python object to make accessible in LaTeX.
        fp (TextIO): The filelike object to write LaTeX code to.
    """
    python2latex(name, obj).save(fp)
