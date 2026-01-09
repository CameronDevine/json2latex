from .escape import escape
import json
from roman import toRoman


__all__ = ["python2latex"]


class python2latex:
    """A class for converting a nested Python structure into a form accessible using
    LaTeX.
    """

    def __init__(self, name, obj):
        """
        Args:
            name (str): The name of the LaTeX variable to save the data to.
            obj (dict or list): The Python object to make accessible in LaTeX.
        """
        self._tex = ""
        self._name = name
        self._check_name(name)
        self._start_convert(obj)

    def _check_name(self, name):
        """Check if variable name is a valid LaTeX macro name.

        .. note::
            Valid LaTeX macro names consist of only lower and uppercase letters.

        Args:
            name (str): The name to check if valid.

        Raises:
            AssertionError: If any characters are not a letter.
        """
        for char in name:
            assert (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122)

    def _start_convert(self, obj):
        """Starts the conversion process.

        Args:
            obj (dict or list): The Python object to make accessible in LaTeX.
        """
        self._tex += "\\makeatletter\n"
        self._to_convert = {0: obj}
        self._index = 1
        while len(self._to_convert):
            self._convert()
        self._tex += "\n\\makeatother"

    def _nl(self, indent=0):
        """Add newline.

        Args:
            indent (int): number of times to indent the next line after the newline, default 0.
        """
        self._tex += "\n" + ("  " * indent)

    def _convert(self):
        """Converts a subset of object.

        This function gets a subset of the object from the ``_to_convert``
        variable and parses it, adding the necessary command to the TeX
        string. If any other possible subsets of the object are possible,
        they are added to the ``_to_convert`` dictionary, for later
        processing.
        """
        ind = list(self._to_convert.keys())[0]
        obj = self._to_convert.pop(ind)

        self._tex += (
            "\\newcommand"
            + self._macro_name(ind)
            + "[1][all]{%"
        )
        self._nl(1)
        self._tex += "\\ifnum\\pdfstrcmp{#1}{all}=0%"
        self._nl(2)

        self._def_out(ind, json.dumps(obj,indent=2))

        self._nl(1)
        self._tex += "\\else%"
        self._nl(2)

        if isinstance(obj, list):
            iterator = enumerate(obj)
        elif isinstance(obj, dict):
            iterator = obj.items()
        self._add_options(ind, iterator)

        self._nl(1)
        self._tex += "\\fi"
        self._nl(1)
        self._tex += self._out_macro_name(ind)
        self._nl()
        self._tex += "}"

    def _add_options(self, ind, iterator):
        """Adds a set of elements to the current command.

        Args:
            ind (int): The index of the current command being created.
            iterator (Iterable): An iterator yielding a tuple of a key or index
                and its corresponding value.
        """
        levels = 0
        for name, value in iterator:
            levels += 1
            self._tex += (
                "\\ifnum\\pdfstrcmp{#1}{"
                + str(name)
                + "}=0%"
            )
            self._nl(3)

            if isinstance(value, (list, dict)):
                self._let_out(ind, self._index)
                self._to_convert.update({self._index: value})
                self._index += 1
            else:
                self._def_out(ind, value)

            self._nl(2)
            self._tex += "\\else%"
            self._nl(3)

        self._def_out(ind, "??")
        self._nl(2)

        self._tex += levels * "\\fi"

    def _macro_name(self, ind):
        """Returns the name of a relay macro.

        Args:
            ind (int): The index to use when creating the macro name.
        """
        if ind > 0:
            return "\\" + self._name + "@" + toRoman(ind)
        else:
            return "\\" + self._name

    def _out_macro_name(self, ind):
        """Returns the name of the output macro.

        Args:
            ind (int): The index to use when creating the macro name.
        """
        return self._macro_name(ind) + "@out"

    def _def_out(self, ind, value):
        """Defines the output macro output to a given value.

        Args:
            ind (int): The index of the ouput macro to set.
            value (Union[str, int, float, bool]): The vale to set the macro to.
        """

        # Start macro
        self._tex += "\\def" + self._out_macro_name(ind) + "{%"

        # Add each part on a separate line with '%' to prevent TeX from
        # introducing spaces
        parts = str(value).splitlines()
        for i, part in enumerate(parts):
            self._nl(indent=2)
            self._tex += escape(part)
            if i < len(parts) - 1:
                self._tex += "%"

        # Close macro
        self._tex += "}%"

    def _let_out(self, ind, relay):
        """Sets the output macro to reference another macro.

        Args:
            ind (int): The index of the output macro to set.
            relay (int): The index of the macro to return.
        """
        self._tex += (
            "\\let"
            + self._out_macro_name(ind)
            + self._macro_name(relay)
            + "%"
        )

    def dump(self):
        """Get the string of LaTeX commands.

        The returned string is a set of LaTeX commands which can be used to
        access the values of the object provided when initializing the class.
        """
        return self._tex

    def save(self, fp):
        """Write the LaTeX commands to a filelike object.

        The string writen includes a set of LaTeX commands which can be used to
        access the values of the object provided when initializing the class.
        """
        fp.write(self.dump())
