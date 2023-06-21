from type import Cube, scrambled_cube, initial_cube
from score import AI_score

for i in range(11):
    print(i, AI_score(scrambled_cube(i)), AI_score(scrambled_cube(i)), AI_score(scrambled_cube(i)))