
# (1b) deline ... code section .....
def deline(a, width=100, header="Array...", prefix="  ."):
    """Remove extraneous lines from array output.
    More useful for long arrays with ndim >= 3

    Requires:
    --------
    `a` : anything
        anything that can be put into array form
    `header` :
        an optional header
    `prefix` : text
        could be just spaces or something like shown
    """
    def _pre(obj):
        for line in obj.splitlines(False):
            frmt = "{}{}".format(prefix, line)
            yield frmt
    # ----
    if not isinstance(a, (list, tuple, np.ndarray)):
        return a
    a = np.asanyarray(a)
    if a.dtype.kind not in ('i', 'u', 'f', 'c'):
        return a
    header += " shape: {} ndim: {}".format(a.shape, a.ndim)
    f1 = (":arr[{}" + ", :{}"*len(a.shape[1:]) + "]")
    out = [header]
    c = 0
    for i in a:
        a_s = f1.format(c, *i.shape)  # ---- uses f1 format above
        out.append(a_s)
        out.extend(_pre(str(i)))
        c += 1
    f = "\n".join([i for i in out if i != prefix])
    with np.printoptions(edgeitems=edge, linewidth=width):
        print(f)
    # ----
