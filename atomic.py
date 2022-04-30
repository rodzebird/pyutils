"""
Provide a bunch of functions around atomic types manipulation.

There are functions to cast values into generic types, validate the type of variables and so on.
"""


import distutils.util

__EXCEPTION_TYPE_INT = "Expecting an int, received a {type}"
__EXCEPTION_TYPE_FLOAT = "Expecting a float, received a {type}"


def areinstance(type, *args):
    """
    Check whether the variables in *args are instances of the given type.
    Perform an isinstance(arg, type) on each of the *args.

    :param type: The type to check for the args.
    :type type: type
    :param args: The list of arguments whose types are checked.
    :type args: tuple

    :return: True if the args are all of the given type, else False.
    :rtype: bool
    """
    for arg in args:
        if not isinstance(arg, type):
            return False
    return True


def is_int(value, raise_on_error=False):
    """
    Check whether the given value is an int or a castable int.

    :param value: The value to cast into an int and check the success.
    :type value: Any

    :return: True if the value is an int, else False.
    :rtype: bool
    """
    is_an_int = to_int(value, None) is not None
    if not is_an_int and raise_on_error is True:
        raise TypeError(__EXCEPTION_TYPE_INT.format(type=type(value)))

    return is_an_int


def is_float(value, raise_on_error=False):
    """
    Check whether the given value is a float or a castable float.

    :param value: The value to cast into a float and check the success.
    :type value: Any

    :return: True if the value is a float, else False.
    :rtype: bool
    """
    is_a_float = to_float(value, None) is not None
    if not is_a_float and raise_on_error is True:
        raise TypeError(__EXCEPTION_TYPE_FLOAT.format(type=type(value)))

    return is_a_float


def unsafe_to_bool(value):
    """
    Really not safe casting to bool.

    Accepts anything, should return a bool or an exception depending on the situation you got yourself into.
    This method acts as a boilerplate for encapsulating methods so please don't use without parental control ; mom always knows what's right for you.
    """
    return bool(distutils.util.strtobool(str(value)))


def to_bool(value, default=None):
    """
    Cast the value to bool. If the value is not a bool, do not raise
    but instead return the default value, by default None.

    :param value: The value to cast into an int.
    :type value: Any
    :param default: The default value to return if the value is not castable.
    :type default: Any

    :return: The value as a bool, or the default value if not castable.
    :rtype: bool or Any
    """
    try:
        return __to__(unsafe_to_bool, value, default)
    except Exception:
        return default


def to_int(value, default=None):
    """
    Cast the value to int. If the value is not an int, do not raise
    but instead return the default value, by default None.

    :param value: The value to cast into an int.
    :type value: Any
    :param default: The default value to return if the value is not castable.
    :type default: Any

    :return: The value as an int, or the default value if not castable.
    :rtype: int or Any
    """
    return __to__(int, value, default)


def to_float(value, default=None):
    """
    Cast the value to float. If the value is not a float, do not raise
    but instead return the default value, by default None.

    :param value: The value to cast into a float.
    :type value: Any
    :param default: The default value to return if the value is not castable.
    :type default: Any

    :return: The value as a float, or the default value if not castable.
    :rtype: float or Any
    """
    return __to__(float, value, default)


def __to__(_type_, value, default=None):
    """
    Cast the value to `_type_`. If the value is not castable to `_type_`,
    do not raise but instead return the default value, by default None.

    :param _type_: The cast in which to cast the given value.
    :type _type_: type
    :param value: The value to cast into `_type_`.
    :type value: Any
    :param default: The default value to return if the value is not castable.
    :type default: Any

    :return: The value as an instance of `_type_`, or the default value
             if not castable.
    :rtype: _type_ or Any
    """
    if value is None:
        return default

    try:
        return _type_(value)
    except ValueError:
        return default
