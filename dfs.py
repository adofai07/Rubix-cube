from type import Cube, scrambled_cube, MOVES
from copy import deepcopy as DC
import sys
from score import AI_score
import time
from mate_in_n_generator import mate_in_n

start_time = time.time()

max_score = -1.8e308
max_score_state = None
max_score_moves = None

def dfs(cube: Cube, max_depth: int=20, moves: list[str]=[], depth: int=0) -> None:
    global max_score, max_score_state, max_score_moves

    if mate_in_n(cube) != -1:
        print(F"[Mate in {mate_in_n(cube)} found]")
        sys.exit(0)

    if max_depth < depth: return

    curr_score = AI_score(cube)

    if curr_score > max_score:
        max_score = curr_score
        max_score_state = cube
        max_score_moves = moves

        print(F"Best so far: {' '.join(max_score_moves) :<60} (score = {max_score :+.02f}) (uptime = {time.time() - start_time :.02f})")

        if max_score > 0:
            sys.exit(0)

    if depth == max_depth:
        return

    print(F"DFS(Cube, [{' '.join(moves)}], {depth})" + " " * 40, end="\r")

    candidates: list[tuple[Cube, str]] = list()

    for move1 in MOVES:
        if depth != 0 and move1[0] == moves[-1][0]: continue

        c = DC(cube)
        c.move(move1)

        candidates.append((c, [move1]))

    if depth == max_depth - 1:
        return

    for move1 in MOVES:
        for move2 in MOVES:
            if depth != 0 and move1[0] == moves[-1][0]: continue
            if depth != 0 and move2[0] == moves[-1][0]: continue

            if depth != 0 and move2[0] == move1[0]: continue

            c = DC(cube)
            c.move(move1)
            c.move(move2)

            candidates.append((c, [move1, move2]))

    if depth == max_depth - 2:
        return

    for move1 in MOVES:
        for move2 in MOVES:
            for move3 in MOVES:
                if depth != 0 and move1[0] == moves[-1][0]: continue
                if depth != 0 and move2[0] == moves[-1][0]: continue
                if depth != 0 and move3[0] == moves[-1][0]: continue

                if depth != 0 and move2[0] == move1[0]: continue
                if depth != 0 and move3[0] == move1[0]: continue
                if depth != 0 and move3[0] == move2[0]: continue

                c = DC(cube)
                c.move(move1)
                c.move(move2)
                c.move(move3)

                candidates.append((c, [move1, move2, move3]))

    candidates.sort(key=lambda x: AI_score(x[0]), reverse=True)
    # random.shuffle(candidates)

    for c in candidates:
        dfs(c[0], max_depth, moves + c[1], depth + len(c[1]))

c = scrambled_cube()

c = Cube([
    "   RGO",
    "   WRW",
    "   GWR",
    "BOYRGBWBWBYY",
    "OBGOWYBGGRYY",
    "GRWGYYBROGOR",
    "   ORO",
    "   BOW",
    "   WBY"
])

print(c)
dfs(c, max_depth=20)
