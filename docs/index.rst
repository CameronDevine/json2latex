JSON to LaTeX
=============

``json2latex`` is a library for converting a nested Python structure to a format
accessible in LaTeX.

.. toctree::
  :maxdepth: 2
  :caption: Contents:

  documentation

Python
------

.. automodule:: json2latex
  :members:

Example
-------

The following Python code saves a file, ``out.tex`` which includes the necessary
LaTeX commands to access the data in LaTeX.

.. code-block:: python

  import json2latex

  data = dict(a="test", b=[1, 2])

  with open('out.tex', 'w') as f:
    json2latex.dump('data', data, f)

The same result can be accomplished by running,

.. code-block:: bash

  json2latex example.json data out.tex

where ``example.json`` is a JSON file containing the same data is the ``data`` dictionary in the Python example.

The code output by JSON to LaTeX can be used as follows. First the file needs to be imported in LaTeX using ``\input{out.tex}``. Then, the following commands can be used to access the data:

- ``\data`` will expand to the full JSON representation of the input, ``{"a": "test", "b": [1, 2]}``.
- ``\data[a]`` will expand to ``test``.
- ``\data[b]`` will expand to ``[1, 2]``.
- ``\data[b][0]`` will expand to ``1``.
- ``\data[b][1]`` will expand to ``2``.
- ``\data[b][2]``, and all other undefined values, will expand to ``??``.
