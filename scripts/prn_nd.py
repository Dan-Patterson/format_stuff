
```
def prn_nd(a, deci=2, width=100, title="Array", prefix="  .", prn=True):
    """Format number arrays by row, and print

    Parameters:
    -----------
    `a` : array
        An array of int or float dtypes, 1, 2, 3 and 4D arrays tested.
    `deci` - int
        Decimal places for floating point numbers
    `width` : int
        Default width for onscreen and printing, output beyond this
        length will be truncated with a warning.  Reshape to overcome.
    `title` : string
        The default title, change to provide more information.

    Returns:
    --------
    Prints the array with the 1st dimension flattened-like by row

    Notes:
    -----
    - `w_frmt` :  width formatter
    - `m_frmt` :  max number formatter to get max. number of characters
    """

    def _concat(rows, r_fmt, width, prefix):
        """print the subset to maximimum width"""
        end = ["", "...."][len(r_fmt.format(*rows[0])) > width]
        txt = prefix
        rw = [r_fmt.format(*v)[:width] + end for v in rows]
        txt += ("\n" + prefix).join(rw)  # + "\n"
        return txt

    def d4_frmt(a_shp, a, txt, a_dim):
        """Dealing with 4, 5 ?D arrays"""
        d4, d, r, c = a_shp
        hdr = "\n" + "-"*25
        fm = hdr + "\n-({}, + ({}, {}, {})"
        if a_dim == 5:
            fm = "\n--(.., {}, + ({}, {}, {})"
        t = ""
        for d3 in range(d4):
            t += fm.format(d3, d, r, c) + "\n"
            a_s = a[d3]
            rows = [a_s[..., i, :].flatten() for i in range(r)]
            t += _concat(rows, row_frmt, width, prefix)
        return t
    #
    # ---- begin constructing the array format ----
    txt = ""
    a = np.asanyarray(a)
    # ---- run _check ----
    if a.ndim < 3:
        if a.ndim == 2:
            a = a.reshape((1,) + a.shape)
        else:
            return "Array is not >= 2D"
    #
    a_shp, a_dim, a_kind, a_min, a_max = _check(a)  # get base array info
    #
    fv = ""
    if np.ma.isMaskedArray(a):  # ----
        a = np.ma.round(a, decimals=deci)
        if a.dtype.kind in floats:
            default_fill = np.ma.default_fill_value(a)
            a.set_fill_value(default_fill)
        else:
            a.set_fill_value(np.iinfo(a.dtype).max)
        fv = ", masked array, fill value {}".format(a.get_fill_value())
        #a = a.data
    # ---- correct dtype, get formats ----
    if (a_kind in nums) and (a_dim >= 3):
        args = title, a_shp, a_dim, fv
        txt = "{}...\n-shape {}, ndim {}{}".format(*args)
        d, r, c = a_shp[-3:]
        row_frmt = _row_format(a, sep='', deci=deci)
        row_frmt = (row_frmt + "  ") * d
        if (a_dim == 3):
            rows = [a[..., i, :].flatten() for i in range(r)]
            txt += "\n" + _concat(rows, row_frmt, width, prefix)
        elif (a_dim == 4):
            d4, d, r, c = a_shp
            t = d4_frmt(a_shp, a, txt, a_dim)
            txt += t
        elif (a_dim == 5):
            d5, d4, d, r, c = a_shp
            hdr = "\n" + "-"*25
            for i in range(d5):
                txt += hdr + '\n--({}, ..'.format(i)
                t = d4_frmt(a_shp[1:], a[i], txt, a_dim)
                txt += t
    else:
        txt = "Only integer and float arrays with ndim >= 2 supported"
    if prn:
        with np.printoptions(precision=deci, linewidth=ln_wdth):
            print(txt)
    else:
        return txt
```
