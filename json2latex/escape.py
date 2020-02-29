def escape(string):
    """
    Replace special characters with their equivalent LaTeX macros.

    Args:
        string (str): The string to process.

    Returns:
        str: The string with special characters replaced with macros.
    """
    replacements = {
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
    escaped = ""
    for char in string:
        escaped += replacements.get(char, char)
    return escaped
