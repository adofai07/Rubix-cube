from type import Cube, initial_cube, MOVES
import tqdm
from copy import deepcopy as DC
import pickle
from path import repo_path

def save(data, thread=0):
    with open(FR"{repo_path}\D{thread}.adofai", "wb+") as f:
        pickle.dump(data, f)

def load(thread=0):
    with open(FR"{repo_path}\D{thread}.adofai", "rb") as f:
        return pickle.load(f)

N = 4

try:
    MATE_IN_N = load(N)
    POSSIBLE_MOVES = load(-N)

except:
    MATE_IN_N = [[initial_cube()]]
    POSSIBLE_MOVES = [[[]]]

    for i in tqdm.trange(1, N + 1, position=0, ascii=True, leave=False):
        MATE_IN_N.append(list())
        POSSIBLE_MOVES.append(list())

        for j in tqdm.trange(len(MATE_IN_N[-2]), position=1, ascii=True, leave=False):
            for move in MOVES:
                c = DC(MATE_IN_N[-2][j])
                c.move(move)

                chk = True

                for k in range(i):
                    if c in MATE_IN_N[k]:
                        chk = False
                        break

                if chk:
                    MATE_IN_N[-1].append(c)
                    POSSIBLE_MOVES[-1].append(POSSIBLE_MOVES[-2][j] + [move])

    save(MATE_IN_N, N)
    save(POSSIBLE_MOVES, -N)

def mate_in_n(c: Cube, m: int=6) -> int:
    for i in range(min(2 * N + 1, m + 1)):
        if _mate_in_n(c, i):
            return i
        
    return -1
    

def _mate_in_n(c: Cube, m: int) -> bool:
    if m <= N:
        return c in MATE_IN_N[m]
    
    if m <= 2 * N:
        for move in POSSIBLE_MOVES[m - N]:
            new_c = DC(c)
            new_c.move_list(move)

            if _mate_in_n(new_c, 4):
                return True
            
        return False

    return False