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
* The score of a state is computed via a DNN model.

## DNN model storing

* The DNN models used in this project have the `.h5` extension.
* The only model remaining has 6 dense layers of size 3125, 625, 125, 25, 5, 1.

## More about the DNN model

The DNN model is made with tensorflow 2.10.0.

```py
model = tf.keras.Sequential([
    tf.keras.layers.Dense(3125, activation='sigmoid', input_shape=(54, )),
    tf.keras.layers.Dense(625, activation='sigmoid'),
    tf.keras.layers.Dense(125, activation='sigmoid'),
    tf.keras.layers.Dense(25, activation='sigmoid'),
    tf.keras.layers.Dense(5, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='linear')
])

model.compile(optimizer="Adam", loss="mse", metrics=[])
```

The model is trained with epochs with 16000 datas each:

```py
I_O = list()

for i in range(16, ascii=True, position=0):
    for j in range(10000, ascii=True, position=1, leave=False):
        I_O.append((scrambled_cube(i).arr[1:], -i))

random.shuffle(I_O)

inputs = np.asarray([i[0] for i in I_O])
outputs = np.asarray([i[1] for i in I_O])

history = model.fit(inputs,
                    outputs,
                    epochs=10,
                    batch_size=10
                    )
```

The goal is to bring the loss function down to 0.1, and the value is currently 3.13. (2023.6.22)
