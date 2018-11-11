
```
def prn_3d4d(a, deci=2, edgeitems=3, width=100, prn=True):
    """Another variant for formatting arrays geared towards 3d and 4d
    numeric and text arrays.  For object, structured arrays, see prn_rec
    in arraytools.frmts
    """
    def _row_format(d, r, c, k, deci, a_min, a_max):
        """abbreviated row format, see frmts.py in arraytools
        """
        if k in nums:
            w_, m_ = [[':{}.0f', '{:0.0f}'], [':{}.{}f', '{:0.{}f}']][k == 'f']
        else:
            w_, m_ = ['!s:>{}', '{}']
            deci = 0
        m = max(len(m_.format(a_max, deci)), len(m_.format(a_min, deci))) + 1
        w_fmt = w_.format(m, deci)
        r_fmt = (('{' + w_fmt + '}') * c + '') * 1  # d
        return r_fmt
    #
    def head_tail(s, e):
        """Keep head and tail of array row/column indices [:e], [-e:]
        if s = 10 and e = 3, then
        h_t => array([ 0,  1,  2, -1,  5,  6,  7]) where -1 is a marker
        """
        h_t = np.arange(s)
        if s > e*2:
            h_t = np.concatenate([h_t[:e], [-1], h_t[-e:]])
        return h_t
    # ---- main section
    # bail?
    if (a.ndim not in (3, 4)) or (a.dtype.kind not in nums):
        msg = "Requires a 3D/4D numeric or text array. Kind in (i, f, U)))"
        print(msg)
        return msg
    # (1) base information and reshape 3D to 4D array
    if a.ndim == 3:
        a = a.reshape((1,) + a.shape)
    s4, s3, s2, s1 = a_shp = a.shape
    # ---- start the format process ----
    # (1) split the indices keeping the row, column edgeitems
    e = edgeitems
    s3_ = head_tail(s3, e)
    s2_ = head_tail(s2, e)
    # (2) assemble information for _row_format
    d_, r_, c_ = a_shp[-3:]
    if a.dtype.kind in ('U', 'S', 'b', 'O', 'V'):
        n = int(a.dtype.str.lstrip('<^>|bOUSV')) #+ 1
        a_min = a_max = int('1'*n)  # cheat to get a number len of string
    elif a.dtype.kind in ('i', 'u', 'f'):
         a_min = a.min()
         a_max = a.max()
    fm0 = _row_format(d_, r_, c_, a.dtype.kind, 2, a_min, a_max)  # d=1
    split_0 = c_ > e*2  # boolean check
    if split_0:  # e in place of c_
        fm1 = _row_format(d_, r_, e, a.dtype.kind, 2, a_min, a_max)
    # (3) process
    t = "Array... ndim {}  shape{}".format(a.ndim, a.shape)
    for k in range(s4):
        for j in s2_:
            row = []
            for i in s3_:
                r_ = a[k][i][j]
                if split_0:
                    sub = fm1.format(*r_[:e]) + " ..." + fm1.format(*r_[-e:])
                else:
                    sub = fm0.format(*r_)
                if (j==-1):
                    row.append("{!s:^{}}".format(" . .", len(sub)))
                else:
                    row.append(sub)
            s = "  ".join(row)
            if len(s) > width:
                s = s[:width] + "..."
            t += "\n|" + s + " |"
        t += "\n|=> ({} {} {} {})\n".format(k, s3, s2, s1)
    if prn:
        print(t)
        return None
    else:
        return t
```
