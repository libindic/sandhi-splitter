
def head_tail(L):
    if len(L) == 0:
        raise IndexError
    elif len(L) == 1:
        return (L[0], [])

    return (L[0], L[1:])
