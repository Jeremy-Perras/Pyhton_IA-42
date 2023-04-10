def ft_reduce(function_to_apply, iterable):
    if (isinstance(iterable, list or tuple)):
        for i, elem in enumerate(iterable):
            if i:
                reduced = function_to_apply(reduced, elem)
            else:
                reduced = elem
        return (reduced)
    try:
        iter(iterable)
        for i, elem in enumerate(iterable):
            if i:
                reduced = function_to_apply(reduced, elem)
            else:
                reduced = elem
        return (reduced)
    except TypeError:

        return
    return
