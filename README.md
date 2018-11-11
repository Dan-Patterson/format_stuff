# format_stuff #
Format options for python and numpy.  I often want a quick print/view of 'stuff' and have found the current offerings not to my needs.  This repository adds to the confusion and options.

Case in point...  remember that... quit the 'but!  what about'

**ugh**
```
ugh = np.random.randint(3*7*11, size=(3, 7, 11))

ugh
 
array([[[ 51, 142, 162, 166,  35,  26, 113,  96, 143, 113,  97],
        [ 55, 134,  60, 106,  75, 180, 201, 101, 146,  25, 167],
        [ 21, 227, 146, 169, 217,  47, 114, 138, 100, 102,  90],
        [120, 193, 214, 194, 144, 114, 214, 221, 108, 134,  72],
        [206, 141,  86,  20,  80, 223, 140, 108,  18, 111, 161],
        [159,  82,  34, 133, 115,  37, 176,  48, 216, 183,  72],
        [205,  17,  79,  62,  72, 193,  30,  81, 121, 210, 211]],

       [[ 97,  65,  50,  88, 106, 122,  25, 214,  11,  11,  57],
        [ 19,  79, 161, 182, 135,  34, 217,  54,  49, 163, 138],
        [ 63, 154,  74, 227,  54, 138,  32, 227,  37,  87, 225],
        [124, 148, 212,  77, 154, 226,  38, 214,  32,  54, 167],
        [ 18,  73,  61,  76, 170,  48, 187, 139,  30, 171, 183],
        [ 48, 151,  27, 122,  27, 230,   7,  49, 152, 184,  20],
        [ 29,  75,  29,   8,  72, 210, 171,  51, 170,  23, 168]],

       [[ 36, 205,  18, 100, 169,  60, 111,  36, 186,  42, 159],
        [199, 178, 227,  89, 177, 211,  87,  51, 157,  69, 170],
        [  5,   4,  50, 116, 125, 129, 185, 219,   0, 117,  29],
        [ 98,  23,  31,   8,  95,  51,  30, 138, 150,  79, 123],
        [  4, 177,  18, 126, 121,  80,  98,  41, 189,  46, 223],
        [196, 201,  38,  22, 150, 123,  95, 210,  51, 100,  25],
        [170,   4, 223,   3,  93, 122, 142, 136, 217, 105, 159]]])
```

**(1) Reshaping the array**

As the array is called ... ugh ... but not bad, at least for small arrays you can see all the numbers.  But the vertical-ness of the presentation gets pretty cumbersome as the dimensions increase or subarray size gets bigger.

You can always reshape the array to scrunch up the rows a tad

```
ugh2 = np.swapaxes(ugh, 0, 1).reshape(shp[1], shp[0]*shp[2])

with np.printoptions(edgeitems=15, linewidth=160):
    print(ugh2)
    
[[ 51 142 162 166  35  26 113  96 143 113  97  97  65  50  88 ... 214  11  11  57  36 205  18 100 169  60 111  36 186  42 159]
 [ 55 134  60 106  75 180 201 101 146  25 167  19  79 161 182 ...  54  49 163 138 199 178 227  89 177 211  87  51 157  69 170]
 [ 21 227 146 169 217  47 114 138 100 102  90  63 154  74 227 ... 227  37  87 225   5   4  50 116 125 129 185 219   0 117  29]
 [120 193 214 194 144 114 214 221 108 134  72 124 148 212  77 ... 214  32  54 167  98  23  31   8  95  51  30 138 150  79 123]
 [206 141  86  20  80 223 140 108  18 111 161  18  73  61  76 ... 139  30 171 183   4 177  18 126 121  80  98  41 189  46 223]
 [159  82  34 133 115  37 176  48 216 183  72  48 151  27 122 ...  49 152 184  20 196 201  38  22 150 123  95 210  51 100  25]
 [205  17  79  62  72 193  30  81 121 210 211  29  75  29   8 ...  51 170  23 168 170   4 223   3  93 122 142 136 217 105 159]]
 ```
 The problem then is you usually run out of print width and the differences in the blocks become less obvious.

**(2) Context managers**
You can use 'context managers' (I think that is what it is called) and if you are working with `numpy`, you can mess with edge items and the like, but keep your main settings intact for most functions and functionality. I did sneak one in, in the previous example you might have noticed.

```
with np.printoptions(edgeitems=3, linewidth=100, precision=2,
                    suppress=True, nanstr='-n-', threshold=100):
    print(ugh)
    
[[[ 51 142 162 ... 143 113  97]
  [ 55 134  60 ... 146  25 167]
  [ 21 227 146 ... 100 102  90]
  ...
  [206 141  86 ...  18 111 161]
  [159  82  34 ... 216 183  72]
  [205  17  79 ... 121 210 211]]

 [[ 97  65  50 ...  11  11  57]
  [ 19  79 161 ...  49 163 138]
  [ 63 154  74 ...  37  87 225]
  ...
  [ 18  73  61 ...  30 171 183]
  [ 48 151  27 ... 152 184  20]
  [ 29  75  29 ... 170  23 168]]

 [[ 36 205  18 ... 186  42 159]
  [199 178 227 ... 157  69 170]
  [  5   4  50 ...   0 117  29]
  ...
  [  4 177  18 ... 189  46 223]
  [196 201  38 ...  51 100  25]
  [170   4 223 ... 217 105 159]]]
  ```
  
The vertical and horizontal scrunchies give you a quick view and who doesn't love ellipses.
  
Often I would rather see things printed more row-wise-ish.

**(3) Removing extra lines**

You can scrunch stuff up!  One of my favourites is `deline`, which does just that, with a tad more about the array as a peace offering.

 ```
deline(ugh)

Array... shape: (3, 7, 11) ndim: 3
:arr[0, :7, :11]
  .[[ 51 142 162 166  35  26 113  96 143 113  97]
  . [ 55 134  60 106  75 180 201 101 146  25 167]
  . [ 21 227 146 169 217  47 114 138 100 102  90]
  . [120 193 214 194 144 114 214 221 108 134  72]
  . [206 141  86  20  80 223 140 108  18 111 161]
  . [159  82  34 133 115  37 176  48 216 183  72]
  . [205  17  79  62  72 193  30  81 121 210 211]]
:arr[1, :7, :11]
  .[[ 97  65  50  88 106 122  25 214  11  11  57]
  . [ 19  79 161 182 135  34 217  54  49 163 138]
  . [ 63 154  74 227  54 138  32 227  37  87 225]
  . [124 148 212  77 154 226  38 214  32  54 167]
  . [ 18  73  61  76 170  48 187 139  30 171 183]
  . [ 48 151  27 122  27 230   7  49 152 184  20]
  . [ 29  75  29   8  72 210 171  51 170  23 168]]
:arr[2, :7, :11]
  .[[ 36 205  18 100 169  60 111  36 186  42 159]
  . [199 178 227  89 177 211  87  51 157  69 170]
  . [  5   4  50 116 125 129 185 219   0 117  29]
  . [ 98  23  31   8  95  51  30 138 150  79 123]
  . [  4 177  18 126 121  80  98  41 189  46 223]
  . [196 201  38  22 150 123  95 210  51 100  25]
  . [170   4 223   3  93 122 142 136 217 105 159]]
  
  ```

**(4) Variants involving the above**

I have variants if I am working with arrays of 3, 4, 5 + dimensions.
For example, the following options allow me to plunk an array row-wise with either clipping, truncation or edge representations.
Not one of them covers all cases, but at least there is an arsenal to choose from.
  
 ```
 # ---- ndim = 3, row-wise
 # ---- option 1 ---- keep the first 'bit' as full as possible, then truncate
 prn_nd(ugh, deci=0, width=100, title="Array", prefix="  .", prn=True)

Array...
-shape (3, 7, 11), ndim 3
  .   51  142  162  166   35   26  113   96  143  113   97     97   65   50   88  106  122   25  214   ....
  .   55  134   60  106   75  180  201  101  146   25  167     19   79  161  182  135   34  217   54   ....
  .   21  227  146  169  217   47  114  138  100  102   90     63  154   74  227   54  138   32  227   ....
  .  120  193  214  194  144  114  214  221  108  134   72    124  148  212   77  154  226   38  214   ....
  .  206  141   86   20   80  223  140  108   18  111  161     18   73   61   76  170   48  187  139   ....
  .  159   82   34  133  115   37  176   48  216  183   72     48  151   27  122   27  230    7   49  1....
  .  205   17   79   62   72  193   30   81  121  210  211     29   75   29    8   72  210  171   51  1....

# ---- option 2 ---- truncate each 'bit' a bit to show more within the width limit

prn_(ugh, deci=2, width=100, title="Array", prefix=". . ", prn=True)

Array... ndim: 3  shape: (3, 7, 11)
. .   51 142 162 166  35  26 113  96..  143 113  97  97  65  50  88 106..  122  25 214  11  11  57  36 2...
. .   55 134  60 106  75 180 201 101..  146  25 167  19  79 161 182 135..   34 217  54  49 163 138 199 1...
. .   21 227 146 169 217  47 114 138..  100 102  90  63 154  74 227  54..  138  32 227  37  87 225   5  ...
. .  120 193 214 194 144 114 214 221..  108 134  72 124 148 212  77 154..  226  38 214  32  54 167  98  ...
. .  206 141  86  20  80 223 140 108..   18 111 161  18  73  61  76 170..   48 187 139  30 171 183   4 1...
. .  159  82  34 133 115  37 176  48..  216 183  72  48 151  27 122  27..  230   7  49 152 184  20 196 2...
. .  205  17  79  62  72 193  30  81..  121 210 211  29  75  29   8  72..  210 171  51 170  23 168 170  ...

# ---- option 3 ---- bring on the ellipses!

prn_3d4d(ugh, deci=0, edgeitems=3, width=100, prn=True)

Array... ndim 4  shape(1, 3, 7, 11)
|  51 142 162 ... 143 113  97    97  65  50 ...  11  11  57    36 205  18 ... 186  42 159 |
|  55 134  60 ... 146  25 167    19  79 161 ...  49 163 138   199 178 227 ... 157  69 170 |
|  21 227 146 ... 100 102  90    63 154  74 ...  37  87 225     5   4  50 ...   0 117  29 |
|             . .                           . .                           . .             |
| 206 141  86 ...  18 111 161    18  73  61 ...  30 171 183     4 177  18 ... 189  46 223 |
| 159  82  34 ... 216 183  72    48 151  27 ... 152 184  20   196 201  38 ...  51 100  25 |
| 205  17  79 ... 121 210 211    29  75  29 ... 170  23 168   170   4 223 ... 217 105 159 |
|=> (0 3 7 11)
```

For arrays with ndim = 4 or above, you can show row-wise and stack column-wise.  Here is another example.
You have your basic array info at the top and a reference to the slice you are looking at.

```
prn_3d4d(d, deci=0, edgeitems=2, width=120, prn=True)
Array... ndim 4  shape(3, 5, 9, 11)
| 141  30 ...   6 119   107  86 ...  23 103    10 174 ... 142   3   187  24 ...  31  55    10 174 ... 142   3 |
| 141 196 ...  84  95   123 193 ...  39  19    47  16 ... 197  12   100  57 ... 163  30    47  16 ... 197  12 |
|         . .                   . .                   . .                   . .                   . .         |
|  40 169 ... 100 134    77  75 ... 185  33    13 107 ... 180  15   175  73 ...  60 124    13 107 ... 180  15 |
|  83   8 ... 119  96   154 105 ...  39 196    20 172 ...  27 175   166 167 ... 105  86    20 172 ...  27 175 |
|=> (0 5 9 11)

| 109  93 ... 160 143    22 126 ... 191 107   157  69 ...  51 141   186   5 ...  76   7   157  69 ...  51 141 |
| 127 168 ... 126  98   154  51 ... 196  85   133 193 ... 162  32    36 153 ... 130  21   133 193 ... 162  32 |
|         . .                   . .                   . .                   . .                   . .         |
| 158 178 ...  63 107    38 157 ...  88 123    80  40 ...  42 115   152 120 ...  86  69    80  40 ...  42 115 |
| 129  20 ...  66  75    64 116 ... 129  24   112 145 ... 138 106   147  27 ... 108 159   112 145 ... 138 106 |
|=> (1 5 9 11)

|  80 184 ...   5 118    99 154 ... 197 198   126 148 ...  62   1    76  47 ... 121 146   126 148 ...  62   1 |
| 106 101 ... 196  56    65 148 ... 174  60    33  16 ... 111  31   176  20 ... 103 136    33  16 ... 111  31 |
|         . .                   . .                   . .                   . .                   . .         |
|  48  74 ...  95 165    33 102 ...  94 177   188  36 ...  17  15    33 175 ...  51   6   188  36 ...  17  15 |
|  86  19 ... 175  65   178 177 ... 156  74   141  83 ...  47 110    16 117 ...  29 185   141  83 ...  47 110 |
|=> (2 5 9 11)
```

**(5) Structured/recarrays?? things get ugh-lier**

Sometimes they look fine, sometimes they are a mangled mess if the columns contain a wide range of character sizes.  This one doesn't look too bad because the sizes are relatively the same.

```
b   # ---- just that messy wrap around but informative presentation
array([( 1,  0, 'B', 'B_', 'Hall', 11), ( 2,  1, 'A', 'A_', 'Hall', 24),
       ( 3,  2, 'C', 'C_', 'Hosp', 43), ( 4,  3, 'A', 'B_', 'Hall', 43),
       ( 5,  4, 'B', 'B_', 'Hall', 16), ( 6,  5, 'B', 'A_', 'Hall',  8),
       ( 7,  6, 'A', 'C_', 'Hall', 26), ( 8,  7, 'B', 'C_', 'Hall', 31),
       ( 9,  8, 'C', 'C_', 'Hall',  7), (10,  9, 'A', 'A_', 'Hall', 58),
       (11, 10, 'A', 'A_', 'Hosp', 20), (12, 11, 'C', 'A_', 'Hosp', 37),
       (13, 12, 'C', 'B_', 'Hall', 36), (14, 13, 'A', 'B_', 'Hosp', 33),
       (15, 14, 'C', 'C_', 'Hosp', 51), (16, 15, 'B', 'C_', 'Hosp', 53),
       (17, 16, 'C', 'A_', 'Hosp', 21), (18, 17, 'C', 'C_', 'Hosp', 42),
       (19, 18, 'A', 'B_', 'Hosp', 43), (20, 19, 'A', 'C_', 'Hall',  5)],
      dtype=[('OBJECTID', '<i4'), ('f0', '<i4'), ('County', '<U2'), ('Town', '<U6'), ('Facility', '<U8'), ('Time', '<i4')])

prn_struct(b, rows_m=3)  # ---- Add some fluff and you have a cute bear-like presentation

OBJECTID   f0    County Town Facility Time  
--------------------------------------------
         1     0 B      B_   Hall         11
         2     1 A      A_   Hall         24
         3     2 C      C_   Hosp         43
        18    17 C      C_   Hosp         42
        19    18 A      B_   Hosp         43
        20    19 A      C_   Hall          5

Array... shape: (20,)
Head/tail rows: 3, columns: 3

prn_rec(b, rows_m=3)  # ---- Koala-like isn't it!!!

 id  OBJECTID   f0    County Town Facility ...
----------------------------------------------
 000          1     0 B      B_   Hall     ...
 001          2     1 A      A_   Hall     ...
 002          3     2 C      C_   Hosp     ...
 003         18    17 C      C_   Hosp     ...
 004         19    18 A      B_   Hosp     ...
 005         20    19 A      C_   Hall     ...
```


**(6) Can't wait?  How about 'prn_q'**. 

This!
```
prn_q(a0, 3)
OID_   ID     Norm    Rank1   Text01 Text02 Xs         Ys         
     1      0   10.83    1393 Ccccc  None    309208.00  5032765.00
     2      1    9.99     650 Bbbbb  eeeee   303006.00  5031740.00
     3      2   10.25    1055 None   None    309797.00  5032586.00
```
Or this!
```
a0[:3] 
array([(1, 0, 10.83, 1393, 'Ccccc', 'None', 309208., 5032765.),
       (2, 1,  9.99,  650, 'Bbbbb', 'eeeee', 303006., 5031740.),
       (3, 2, 10.25, 1055, 'None', 'None', 309797., 5032586.)],
      dtype=[('OID_', '<i4'), ('ID', '<i4'), ('Norm', '<f8'), ('Rank1', '<i4'), ('Text01', '<U5'), ('Text02', '<U5'), ('Xs', '<f8'), ('Ys', '<f8')])
```
Quick and fast and suitable for small arrays.

**Options abound.**

See [reshape_options...](../blob/master/reshape_options.py) for the code used to generate the array shapes contained in the image below.

<a href="url"><img src="https://github.com/Dan-Patterson/format_stuff/blob/master/array_shapes.png" ></a>

**The code will follow**

