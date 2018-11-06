
**column kind and width **

# ----------------------------------------------------------------------
# (1h) _c_kind_width .... code section
#
def _col_kind_width(a, deci=0):
    """Column properties for recarray/structured array types.
    This is normally called when examining their properties.

    Notes:
        Used by _col_format, hence prn_rec and prn_struct.  It check the
    length of the values in the field, rounded to `deci`mal places if needed,
    the it compares that value to the field name length and returns the `max`.

    You can check a whole array, `a`, using:
    >>> [_col_kind_width(col) for col in [a[name] for name in a.dtype.names]]
    [('i', 5), ('U', 25), ('i', 5), ('i', 5)]
    """
    def _ckw_(a, name, deci):
        """process for arrays arrays with named fields"""
        c_kind = a.dtype.kind
        if (c_kind in floats) and (deci != 0):  # float with decimals
            c_max, c_min = np.round([a.min(), a.max()], deci)
            c_width = len(max(str(c_min), str(c_max), key=len))
        elif c_kind in nums:      # int, unsigned int, float wih no decimals
            c_width = len(max(str(a.min()), str(a.max()), key=len))
        elif c_kind in ('U', 'S', 's'):
            c_width = len(max(a, key=len))
        else:
            c_width = len(str(a))
        c_width = max(len(name), c_width)
        return [c_kind, c_width]
    # ---- constants
    floats = np.typecodes['AllFloat']
    ints = np.typecodes['AllInteger']
    nums = floats + ints
    # ---- call to _ckw_ ----
    dtn = a.dtype.names
    if dtn is None:  # ---- uniform dtype
        return [_ckw_(a, deci)]
    else:  # ---- mixed dtype with names
        return [_ckw_(a[name], name, deci) for name in dtn]
