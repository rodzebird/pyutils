import inspect
import warnings
import functools


def __deprecated_funclass__(funclass, warning):
    @functools.wraps(funclass)
    def wrapper(*args, **kwargs):
        warnings.simplefilter("always", DeprecationWarning)
        warnings.warn(warning, category=DeprecationWarning, stacklevel=2)
        warnings.simplefilter("default", DeprecationWarning)
        return funclass(*args, **kwargs)

    return wrapper


def deprecated(reason):
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.

    :param reason: A reason given to explain why the entity is deprecated.
                   If not given, the `reason` argument can contain either
                   a function or a class, which will change the behaviour
                   of the decorator; see below.
    :type reason: str or function or class
    """

    if isinstance(reason, str):

        def decorator(funclass):
            warning = "Call to deprecated {} {} ({})"
            warning = warning.format("class" if inspect.isclass(funclass) else "function", funclass.__name__, reason)
            return __deprecated_funclass__(funclass, warning)

        return decorator

    # In this case, no reason is given and thus the `reason` argument is
    # either a function or a class, like in any classic decorator.
    if inspect.isclass(reason) or inspect.isfunction(reason):
        warning = "Call to deprecated {} {}"
        warning = warning.format("class" if inspect.isclass(reason) else "function", reason.__name__)
        return __deprecated_funclass__(reason, warning)
    else:
        raise TypeError(repr(type(reason)))
