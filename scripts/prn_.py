
```
def prn_(a, deci=2, width=100, title="Array", prefix=". . ", prn=True):
    """Alternate format to prn_nd function.
    Inputs are largely the same.
    """
    def _piece(sub, i, frmt, linewidth):
        """piece together 3D chunks by row"""
        s0 = sub.shape[0]
        block = np.hstack([sub[j] for j in range(s0)])
        txt = ""
        if i is not None:
            fr = (":arr[{}" + ", :{}"*len(a.shape[1:]) + "]\n")
            txt = fr.format(i, *sub.shape)
        for line in block:
            ln = frmt.format(*line)[:linewidth]
            end = ["\n", "...\n"][len(ln) >= linewidth]
            txt += indent(ln + end, ". . ")
        return txt
    # ---- main section ----
    out = "\n{}... ndim: {}  shape: {}\n".format(title, a.ndim, a.shape)
    linewidth = width
    if a.ndim <= 1:
        return a
    elif a.ndim == 2:
        a = a.reshape((1,) + a.shape)
    # ---- pull the 1st and 3rd dimension for 3D and 4D arrays
    frmt = make_row_format(dim=a.shape[-3],
                           cols=a.shape[-1],
                           a_kind=a.dtype.kind,
                           deci=deci,
                           a_max=a.max(),
                           a_min=a.min(),
                           width=width,
                           prn=False)
    if a.ndim == 3:
        s0, s1, s2 = a.shape
        out += _piece(a, None, frmt, linewidth)  # ---- _piece ----
    elif a.ndim == 4:
        s0, s1, s2, _ = a.shape
        for i in range(s0):
            out = out + "\n" + _piece(a[i], i, frmt, linewidth)  # ---- _piece
    if prn:
        with np.printoptions(precision=deci, linewidth=width):
            print(out)
    else:
        return out
        ```
