def ft_filter(function_to_apply, iterable):
    try:
        iter(iterable)
        return (i for i in iterable if function_to_apply(i))
    except TypeError:
        return
    return
