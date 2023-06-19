# Rubix-cube

## About the Rubik's cube

Wikipedia: <https://en.wikipedia.org/wiki/Rubik%27s_Cube>

The Rubik's Cube is a 3-D combination puzzle originally invented in 1974 by Hungarian sculptor and professor of architecture Ernő Rubik.

## Initial configuration

* The 6 colors are standardized to white, red, blue, orange, green, and yellow.
* Also, they should be white opposite yellow, blue opposite green, and orange opposite red, and red, white, and blue arranged clockwise in that order.

## Cube type

A cube is stored using a 55-length list, each index indicating positions below:

```py
[  ] [  ] [  ] [10] [11] [12] [  ] [  ] [  ] [  ] [  ] [  ]
[  ] [  ] [  ] [13] [14] [15] [  ] [  ] [  ] [  ] [  ] [  ]
[  ] [  ] [  ] [16] [17] [18] [  ] [  ] [  ] [  ] [  ] [  ]
[37] [38] [39] [ 1] [ 2] [ 3] [19] [20] [21] [46] [47] [48]
[40] [41] [42] [ 4] [ 5] [ 6] [22] [23] [24] [49] [50] [51]
[43] [44] [45] [ 7] [ 8] [ 9] [25] [26] [27] [52] [53] [54]
[  ] [  ] [  ] [28] [29] [30] [  ] [  ] [  ] [  ] [  ] [  ]
[  ] [  ] [  ] [31] [32] [33] [  ] [  ] [  ] [  ] [  ] [  ]
[  ] [  ] [  ] [34] [35] [36] [  ] [  ] [  ] [  ] [  ] [  ]
```

* Each color is transposed into an integer from 0 to 5.
* The index 0 is not used for simplicity.

## Notations

This program uses the **Singmaster notation**.

* Each clockwise turn is indicated by L, R, F, B, U, D.
* Each counterclockwise turn is indicated by L', R', F', B', U', D'.
* Each half turn is indicated by L2, R2, F2, B2, U2, D2.

## Scores

* The score of a cube state is a float which we have to maximize.
* The score-calculating algorithm varies depending on the `type` argument.
