
def prn_q(a, rows=None, deci=2):
    """Quick print a structured array.

    rows : None or integer
        None, prints all the rows. If an integer, prints [:rows] of the array.
    deci : integer
        Number of decimal places to use for float values.
    """
    cf = _col_format(a, deci=deci)  # ---- the big work done here
    frmt = " ".join(['{' + i[0] + '}' for i in cf])
    hdr = " ".join(['{!s:<' + str(i[1]) + '}' for i in cf])
    if rows is None:
        rows = a.shape[0]
    print(hdr.format(*a.dtype.names))
    for row in range(rows):
        print(frmt.format(*a[row]))
