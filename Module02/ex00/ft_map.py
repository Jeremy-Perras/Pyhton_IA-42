def ft_map(function_to_apply, iterable):
    try:
        iter(iterable)
        for i in iterable:
            return (function_to_apply(i) for i in iterable)
    except TypeError:
        return
    return
