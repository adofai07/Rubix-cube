class Cube:
    def __init__(self, c: list[str]):
        self.chrset = []

        for i in c:
            for j in i:
                if j != " " and j not in self.chrset:
                    self.chrset.append(j)
        
        assert len(self.chrset) == 6

        self.arr = [None,
                    c[3][3], c[3][4], c[3][5], c[4][3], c[4][4], c[4][5], c[5][3], c[5][4], c[5][5],
                    c[0][3], c[0][4], c[0][5], c[1][3], c[1][4], c[1][5], c[2][3], c[2][4], c[2][5],
                    c[3][6], c[3][7], c[3][8], c[4][6], c[4][7], c[4][8], c[5][6], c[5][7], c[5][8],
                    c[6][3], c[6][4], c[6][5], c[7][3], c[7][4], c[7][5], c[8][3], c[8][4], c[8][5],
                    c[3][0], c[3][1], c[3][2], c[4][0], c[4][1], c[4][2], c[5][0], c[5][1], c[5][2],
                    c[3][9], c[3][10], c[3][11], c[4][9], c[4][10], c[4][11], c[5][9], c[5][10], c[5][11]
                    ]
        
        for i in range(55):
            for j in range(6):
                if self.arr[i] == self.chrset[j]:
                    self.arr[i] = j

    def move(self, move: str) -> None:
        if len(move) == 1:
            rep = 1

        if move[-1] == "2":
            rep = 2

        if move[-1] == "'":
            rep = 3

        if move == "L":
            for _ in range(rep):
                self.arr[37], self.arr[38], self.arr[39], self.arr[40], self.arr[42], self.arr[43], self.arr[44], self.arr[45], self.arr[10], self.arr[13], self.arr[16], self.arr[1], self.arr[4], self.arr[7], self.arr[28], self.arr[31], self.arr[34], self.arr[54], self.arr[51], self.arr[48] = self.arr[43], self.arr[40], self.arr[37], self.arr[44], self.arr[38], self.arr[45], self.arr[42], self.arr[39], self.arr[54], self.arr[51], self.arr[48], self.arr[10], self.arr[13], self.arr[16], self.arr[1], self.arr[4], self.arr[7], self.arr[28], self.arr[31], self.arr[34]

        if move == "R":
            for _ in range(rep):
                self.arr[19], self.arr[20], self.arr[21], self.arr[22], self.arr[24], self.arr[25], self.arr[26], self.arr[27], self.arr[18], self.arr[15], self.arr[12], self.arr[46], self.arr[49], self.arr[52], self.arr[36], self.arr[33], self.arr[30], self.arr[9], self.arr[6], self.arr[3] = self.arr[25], self.arr[22], self.arr[19], self.arr[26], self.arr[20], self.arr[27], self.arr[24], self.arr[21], self.arr[9], self.arr[6], self.arr[3], self.arr[18], self.arr[15], self.arr[12], self.arr[46], self.arr[49], self.arr[52], self.arr[36], self.arr[33], self.arr[30]

        if move == "F":
            for _ in range(rep):
                self.arr[1], self.arr[2], self.arr[3], self.arr[4], self.arr[6], self.arr[7], self.arr[8], self.arr[9], self.arr[16], self.arr[17], self.arr[18], self.arr[19], self.arr[22], self.arr[25], self.arr[30], self.arr[29], self.arr[28], self.arr[45], self.arr[42], self.arr[39] = self.arr[7], self.arr[4], self.arr[1], self.arr[8], self.arr[2], self.arr[9], self.arr[6], self.arr[3], self.arr[45], self.arr[42], self.arr[39], self.arr[16], self.arr[17], self.arr[18], self.arr[19], self.arr[22], self.arr[25], self.arr[30], self.arr[29], self.arr[28]

        if move == "B":
            for _ in range(rep):
                self.arr[46], self.arr[47], self.arr[48], self.arr[49], self.arr[51], self.arr[52], self.arr[53], self.arr[54], self.arr[12], self.arr[11], self.arr[10], self.arr[37], self.arr[40], self.arr[43], self.arr[34], self.arr[35], self.arr[36], self.arr[27], self.arr[24], self.arr[21] = self.arr[52], self.arr[49], self.arr[46], self.arr[53], self.arr[47], self.arr[54], self.arr[51], self.arr[48], self.arr[27], self.arr[24], self.arr[21], self.arr[12], self.arr[11], self.arr[10], self.arr[37], self.arr[40], self.arr[43], self.arr[34], self.arr[35], self.arr[36]

        if move == "U":
            for _ in range(rep):
                self.arr[10], self.arr[11], self.arr[12], self.arr[13], self.arr[15], self.arr[16], self.arr[17], self.arr[18], self.arr[48], self.arr[47], self.arr[46], self.arr[21], self.arr[20], self.arr[19], self.arr[3], self.arr[2], self.arr[1], self.arr[39], self.arr[38], self.arr[37] = self.arr[16], self.arr[13], self.arr[10], self.arr[17], self.arr[11], self.arr[18], self.arr[15], self.arr[12], self.arr[39], self.arr[38], self.arr[37], self.arr[48], self.arr[47], self.arr[46], self.arr[21], self.arr[20], self.arr[19], self.arr[3], self.arr[2], self.arr[1]

        if move == "D":
            for _ in range(rep):
                self.arr[28], self.arr[29], self.arr[30], self.arr[31], self.arr[33], self.arr[34], self.arr[35], self.arr[36], self.arr[7], self.arr[8], self.arr[9], self.arr[25], self.arr[26], self.arr[27], self.arr[52], self.arr[53], self.arr[54], self.arr[43], self.arr[44], self.arr[45] = self.arr[34], self.arr[31], self.arr[28], self.arr[35], self.arr[29], self.arr[36], self.arr[33], self.arr[30], self.arr[43], self.arr[44], self.arr[45], self.arr[7], self.arr[8], self.arr[9], self.arr[25], self.arr[26], self.arr[27], self.arr[52], self.arr[53], self.arr[54]

    def __str__(self) -> str:
        return F"   {self.arr[10]}{self.arr[11]}{self.arr[12]}\n   {self.arr[13]}{self.arr[14]}{self.arr[15]}\n   {self.arr[16]}{self.arr[17]}{self.arr[18]}\n{self.arr[37]}{self.arr[38]}{self.arr[39]}{self.arr[1]}{self.arr[2]}{self.arr[3]}{self.arr[19]}{self.arr[20]}{self.arr[21]}{self.arr[46]}{self.arr[47]}{self.arr[48]}\n{self.arr[40]}{self.arr[41]}{self.arr[42]}{self.arr[4]}{self.arr[5]}{self.arr[6]}{self.arr[22]}{self.arr[23]}{self.arr[24]}{self.arr[49]}{self.arr[50]}{self.arr[51]}\n{self.arr[43]}{self.arr[44]}{self.arr[45]}{self.arr[7]}{self.arr[8]}{self.arr[9]}{self.arr[25]}{self.arr[26]}{self.arr[27]}{self.arr[52]}{self.arr[53]}{self.arr[54]}\n   {self.arr[28]}{self.arr[29]}{self.arr[30]}\n   {self.arr[31]}{self.arr[32]}{self.arr[33]}\n   {self.arr[34]}{self.arr[35]}{self.arr[36]}"

    def move_list(self, moves: list[str]) -> None:
        for move in moves:
            self.move(move)
