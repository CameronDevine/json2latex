_replacements = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\^{}",
    "\\": r"\textbackslash{}",
    "\n": "\\newline%\n",
    "-": r"{-}",
    "\xA0": "~",  # Non-breaking space
    "[": r"{[}",
    "]": r"{]}",
}
_replacement_lookup = str.maketrans(_replacements)

def escape(string):
    """
    Replace special characters with their equivalent LaTeX macros.

    Args:
        string (str): The string to process.

    Returns:
        str: The string with special characters replaced with macros.
    """
    return string.translate(_replacement_lookup)
