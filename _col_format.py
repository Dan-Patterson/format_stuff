

# (1i) _col_format .... code section
#
def _col_format(c, c_name="c00", deci=0):
    """Determine column format given for an ndarray or structured array.  The
    number of decimal places for float fields can be specified.
    Used by prn_rec.

    `c` : column
        A column in an array.
    `c_name` : text
        column name for ndarrays of uniform dtype.  Ignored otherwise
    `deci` : int
        Desired number of decimal points if the data are numeric

    Requires:
    ---------
    _col_kind_width : function
        This function does the determination of column kind and width

    Notes:
    -----
    To do all field `names`

    >>> [_col_format(j) for j in [a[i] for i in names]]
    [(':> 6.0f', 5), ('!s:<26', 25), (':> 6.0f', 5),
     (':> 6.0f', 5), (':> 4.0f', 2)]
    >>> # c_format, c_width

    The field is examined to determine whether it is a simple integer, a
    float type or a list, array or string.  The maximum width is determined
    based on this type.

    Checks were also added for (N,) shaped structured arrays being
    reformatted to (N, 1) shape which sometimes occurs to facilitate array
    viewing.  A kludge at best, but it works for now.
    """
    pairs = _col_kind_width(c, deci=deci)
    form_width = []
    for c_kind, c_width in pairs:
        if c_kind in ('i', 'u'):  # ---- integer type
            w_ = ':> {}.0f'
            c_width = max(len(c_name), c_width) + deci
            c_format = w_.format(c_width, 0)
        elif c_kind == 'f' and np.isscalar(c[0]):  # ---- float type with rounding
            w_ = ':> {}.{}f'
            c_width = max(len(c_name), c_width) + deci
            c_format = w_.format(c_width, deci)
        else:
            c_format = "!s:<{}".format(c_width)
        form_width.append([c_format, c_width])
    return form_width
