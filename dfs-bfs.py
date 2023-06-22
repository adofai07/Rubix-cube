from type import Cube, scrambled_cube, MOVES
from copy import deepcopy as DC
import sys
import random
from score import AI_score
from collections import deque

# dfs_max_score = -1.8e308
dfs_max_score_state = None
dfs_max_score_moves = []
dfs_nodes = 0

# bfs_max_score = -1.8e308
bfs_max_score_state = None
bfs_max_score_moves = []

global_max_score = -1.8e308

def dfs(cube: Cube, max_depth: int=20, max_nodes: int=1000000000000000, moves: list[str]=[], depth: int=0) -> None:
    global global_max_score, dfs_max_score_state, dfs_max_score_moves, dfs_nodes

    if max_depth < depth: return
    if depth == 0: dfs_nodes = 1
    else: dfs_nodes += 1
    if dfs_nodes > max_nodes: return

    curr_score = AI_score(cube)

    if curr_score > global_max_score:
        global_max_score = curr_score
        dfs_max_score_state = cube
        dfs_max_score_moves = bfs_max_score_moves + moves

        print(F"Best so far (dfs): {' '.join(dfs_max_score_moves) :<60} (nodes = {dfs_nodes}) (score = {global_max_score :+.02f})")

        if global_max_score > 0:
            sys.exit(0)

    # print(F"DFS(Cube, {moves}, {depth})")

    candidates: list[tuple[Cube, str]] = list()

    for move in MOVES:
        if depth != 0 and move[0] == moves[-1][0]: continue

        c = DC(cube)
        c.move(move)

        candidates.append((c, move))

    candidates.sort(key=lambda x: x[0].score(1), reverse=True)
    random.shuffle(candidates)

    for c in candidates:
        dfs(c[0], max_depth, max_nodes, moves + [c[1]], depth + 1)

def bfs(cube: Cube, max_depth: int=3):
    global global_max_score, bfs_max_score_state, bfs_max_score_moves

    DQ = deque()
    DQ.append((cube, []))

    for depth in range(max_depth):
        for i in range(len(DQ)):
            left = DQ.popleft()

            for move in MOVES:
                c = DC(left[0])
                c.move(move)

                DQ.append((c, left[1] + [move]))

                if AI_score(c) > global_max_score:
                    global_max_score = AI_score(c)
                    bfs_max_score_state = c
                    bfs_max_score_moves = dfs_max_score_moves + left[1] + [move]

                    print(F"Best so far (bfs): {' '.join(bfs_max_score_moves) :<66} (score = {global_max_score :+.02f})")


c = scrambled_cube()

c = Cube([
    "   YOY",
    "   OBO",
    "   WRY",
    "RWGRYOBGRGYB",
    "GWWBRWRYBROY",
    "OWOGYRWBGOGW",
    "   YBB",
    "   GGO",
    "   BRW"
])

dfs_max_score_state = c
bfs_max_score_state = c
global_max_score = AI_score(c)

print(c)

bfs(bfs_max_score_state, max_depth=2)

print("DFS ---")
dfs(bfs_max_score_state, max_depth=20)