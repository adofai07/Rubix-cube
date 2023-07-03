from type import Cube, initial_cube, MOVES
import tqdm
from copy import deepcopy as DC
import pickle
from path import repo_path
import bisect

BSL = bisect.bisect_left
BSR = bisect.bisect_right

def save(data, thread=0):
    with open(FR"{repo_path}\D{thread}.adofai", "wb+") as f:
        pickle.dump(data, f)

def load(thread=0):
    with open(FR"{repo_path}\D{thread}.adofai", "rb") as f:
        return pickle.load(f)

N = 6

POSSIBLE_MOVES = load(-4)

try:
    MATE_IN_N = load(N)

except:
    MATE_IN_N_ = load(N - 1)

    for i in tqdm.trange(N, N + 1, position=0, ascii=True, leave=False):
        MATE_IN_N_.append(list())

        for j in tqdm.trange(len(MATE_IN_N_[-2]), position=1, ascii=True, leave=False):
            for move in MOVES:
                c = DC(MATE_IN_N_[-2][j])
                c.move(move)

                MATE_IN_N_[-1].append(c)

    for i in range(N + 1):
        MATE_IN_N_[i].sort()

    MATE_IN_N = list()

    for i in tqdm.trange(N + 1, position=0, ascii=True, leave=False):
        MATE_IN_N.append(list())

        for j in tqdm.trange(len(MATE_IN_N_[i]), position=1, ascii=True, leave=False):
            if j == 0 and MATE_IN_N_[i][j] != MATE_IN_N_[i][j - 1]:
                    chk = True

                    for k in range(N):
                        if BSR(MATE_IN_N_[k], MATE_IN_N_[i][j]) - BSL(MATE_IN_N_[k], MATE_IN_N_[i][j]) >= 1:
                            chk = False
                            break

                    if chk:
                        MATE_IN_N[-1].append(MATE_IN_N_[i][j])

    save(MATE_IN_N, N)

def mate_in_n(c: Cube, m: int=N+2) -> int:
    for i in range(min(m + 1, 2 * N + 1)):
        if _mate_in_n(c, i):
            return i

    return -1
    

def _mate_in_n(c: Cube, m: int) -> bool:
    if m <= N:
        return BSR(MATE_IN_N[m], c) - BSL(MATE_IN_N[m], c) >= 1
    
    if m <= 2 * N:
        for move in POSSIBLE_MOVES[m - N]:
            new_c = DC(c)
            new_c.move_list(move)

            if _mate_in_n(new_c, N):
                return True
            
        return False

    return False