```
def shape_to2D(a, stack2D=True, by_column=False):
    """Reshape an ndim array to a 2D array for print formatting and other uses.

    a : array
        array ndim >= 3
    stack2D : boolean
      True, swaps, then stacks the last two dimensions row-wise.

      False, the first two dimensions are raveled then vertically stacked

    >>> shp = (2, 2, 3)
    >>> a = np.arange(np.prod(shp)).reshape(shp)
    array([[[ 0,  1,  2],
            [ 3,  4,  5]],
           [[ 6,  7,  8],
            [ 9, 10, 11]]])

    2D stack by row

    >>> re_shape(a, stack2D=True,  by_column=False)  # np.hstack((a[0], a[1]))
    array([[ 0,  1,  2,  6,  7,  8],
           [ 3,  4,  5,  9, 10, 11]])

    2D stack raveled by row

    >>> re_shape(a, stack2D=False, by_column=False)
    array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11]])

    2D stack by column

    >>> re_shape(a, True, True)
    array([[ 0,  3],
           [ 1,  4],
           [ 2,  5],  # note here a[0] is translated and stacked onto a[1]
           [ 6,  9],
           [ 7, 10],
           [ 8, 11]])

    >>>  re_shape(a, False, True)
    array([[ 0,  6],
           [ 1,  7],
           [ 2,  8],  # note here a[0] becomes raveled and translated and
           [ 3,  9],  # a[1] is stacked column-wise to it.
           [ 4, 10],
           [ 5, 11]])

    For other shapes::

        shp          re_shape(a).shape
        (3, 4)       (4, 3)
        (2, 3, 4)    (3, 8)
        (2, 3, 4, 5) (3, 40)

    np.transpose and np.swapaxes are related

    >>> np.all(np.swapaxes(a, 0, 1) == np.transpose(a, (1, 0, 2)))
    """
    shp = a.shape
    if stack2D:
        out = np.swapaxes(a, 0, 1).reshape(shp[1], np.prod((shp[0],) + shp[2:]))
    else:
        m = 2
        n = len(shp) - m
        out = a.reshape(np.prod(shp[:n], dtype='int'), np.prod(shp[-m:]))
    if by_column:
        out = out.T
    return out
```
