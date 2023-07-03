from type import Cube, scrambled_cube, MOVES
from copy import deepcopy as DC
import sys
from score import AI_score
import time
from mate_in_n_generator import mate_in_n

start_time = time.time()

max_score = -1.8e308
max_score_state = None
max_score_moves = []

def mate_found(c: Cube) -> list[str]:
    M = mate_in_n(c)
    if M == 0: return []

    else:
        for move in MOVES:
            new_c = DC(c)

            new_c.move(move)

            if mate_in_n(new_c) == M - 1:
                return [move] + mate_found(new_c)

def dfs(cube: Cube, max_depth: int=20, moves: list[str]=[], depth: int=0) -> None:
    global max_score, max_score_state, max_score_moves

    if max_depth < depth: return

    curr_score = AI_score(cube)

    if curr_score > max_score:
        max_score = curr_score
        max_score_state = cube
        max_score_moves = moves

        print(F"Best so far: {' '.join(max_score_moves) :<60} (score = {max_score :+.02f}) (uptime = {time.time() - start_time :.0f})")

        if max_score > 0:
            sys.exit(0)

    if mate_in_n(cube) != -1:
        print(F"{' '.join(max_score_moves)} -> [Can be solved in {mate_in_n(cube)} moves] [{' '.join(mate_found(cube))}]")
        sys.exit(0)

    print_string = F"DFS(Cube, [{' '.join(moves)}], {depth})"

    print(print_string + " " * 40, end="\r")

    if depth == max_depth:
        return

    if depth < max_depth:
        candidates: list[tuple[Cube, str]] = list()

        for move1 in MOVES:
            if depth != 0 and move1[0] == moves[-1][0]: continue
            print(print_string + F" {move1}" + " " * 40, end="\r")

            c = DC(cube)
            c.move(move1)

            candidates.append((c, [move1], AI_score(c)))

    if depth < max_depth - 1:
        for move1 in MOVES:
            for move2 in MOVES:
                if depth != 0 and move1[0] == moves[-1][0]: continue
                if depth != 0 and move2[0] == moves[-1][0]: continue

                if move2[0] == move1[0]: continue
                print(print_string + F" {move1} {move2}" + " " * 40, end="\r")

                c = DC(cube)
                c.move(move1)
                c.move(move2)

                candidates.append((c, [move1, move2], AI_score(c)))

    # if depth < max_depth - 2:
    #     for move1 in MOVES:
    #         for move2 in MOVES:
    #             for move3 in MOVES:
    #                 if depth != 0 and move1[0] == moves[-1][0]: continue
    #                 if depth != 0 and move2[0] == moves[-1][0]: continue
    #                 if depth != 0 and move3[0] == moves[-1][0]: continue

    #                 if move2[0] == move1[0]: continue
    #                 if move3[0] == move1[0]: continue
    #                 if move3[0] == move2[0]: continue
    #                 print(print_string + F" {move1} {move2} {move3}" + " " * 40, end="\r")

    #                 c = DC(cube)
    #                 c.move(move1)
    #                 c.move(move2)
    #                 c.move(move3)

    #                 candidates.append((c, [move1, move2, move3], AI_score(c)))

    candidates.sort(key=lambda x: x[2], reverse=True)
    # random.shuffle(candidates)

    if candidates[0][2] < curr_score:
        return

    for c in candidates:
        dfs(c[0], max_depth, moves + c[1], depth + len(c[1]))

c = scrambled_cube(20, print_moves=True)

# c = Cube([
#     "   BYO",
#     "   WWY",
#     "   RWG",
#     "YRGYBRWOGWGR",
#     "BOGRGRYROWBY",
#     "YWBWGBORWBOG",
#     "   OOY",
#     "   GYB",
#     "   OBR"
# ])

print(c)
dfs(c, max_depth=11)
