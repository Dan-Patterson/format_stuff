```
def reshape_options(a):
    """Alternative shapes for a numpy array.

    Parameters:
    -----------
    a : ndarray
        The ndarray with ndim >= 2

    Returns:
    --------
    An object array containing the shapes of equal or lower dimension,
    excluding ndim=1

    >>> a.shape # => (3, 2, 4)
    array([(2, 12), (3, 8), (4, 6), (6, 4), (8, 3), (12, 2), (2, 3, 4),
           (2, 4, 3), (3, 2, 4), (3, 4, 2), (4, 2, 3), (4, 3, 2)],
          dtype=object)

    Notes:
    ------
    >>> s = list(a.shape)
    >>> case = np.array(list(chain.from_iterable(permutations(s, r)
                        for r in range(len(s)+1)))[1:]
    >>> prod = [np.prod(i) for i in case]
    >>> match = np.where(prod == size)[0]

    References:
    -----------
    `<https://docs.python.org/3/library/itertools.html#itertools-recipes>`
    """
    from itertools import permutations, chain
    s = list(a.shape)
    case0 = np.array(list(chain.from_iterable(permutations(s, r)
                    for r in range(len(s)+1)))[1:])
    case1 = [i + (-1,) for i in case0]
    new_shps = [a.reshape(i).shape for i in case1]
    z = [i[::-1] for i in new_shps]
    new_shps = new_shps + z
    new_shps = [i for i in np.unique(new_shps) if 1 not in i]
    new_shps = np.array(sorted(new_shps, key=len, reverse=False))
    return new_shps
    ```
