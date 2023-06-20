from type import Cube, scrambled_cube, MOVES
from copy import deepcopy as DC
import sys
from score import AI_score

max_score = -1.8e308
max_score_state = None
max_score_moves = None

def dfs(cube: Cube, max_depth: int=20, moves: list[str]=[], depth: int=0) -> None:
    global max_score, max_score_state, max_score_moves

    if max_depth < depth: return

    curr_score = AI_score(cube)

    if curr_score > max_score:
        max_score = curr_score
        max_score_state = cube
        max_score_moves = moves

        print(F"Best so far: {' '.join(max_score_moves) :<60} (score = {max_score :+.02f})")

        if max_score > 0:
            sys.exit(0)

    # print(F"DFS(Cube, {moves}, {depth})")

    candidates: list[tuple[Cube, str]] = list()

    for move in MOVES:
        if depth != 0 and move[0] == moves[-1][0]: continue

        c = DC(cube)
        c.move(move)

        candidates.append((c, move))

    candidates.sort(key=lambda x: x[0].score(1), reverse=True)
    # random.shuffle(candidates)

    for c in candidates:
        dfs(c[0], max_depth, moves + [c[1]], depth + 1)

c = scrambled_cube()

print(c)
dfs(c, max_depth=20)
