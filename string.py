"""
Provide a bunch of functions around string manipulation.
"""


def to_class_case(module):
    """
    Return the module name as a class name, from snake_case to PascalCase.

    :param module: A module name in snake_case.
    :type module: str

    :return: A class name associated to the module.
    :rtype: str
    """
    return module.title().replace("_", "")
