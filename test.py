from type import Cube, scrambled_cube, initial_cube
from score import AI_score
from mate_in_n_generator import mate_in_n

for i in range(16):
    print(i, AI_score(scrambled_cube(i)), AI_score(scrambled_cube(i)), AI_score(scrambled_cube(i)))

print(mate_in_n(scrambled_cube(1)))
print(mate_in_n(scrambled_cube(2)))
print(mate_in_n(scrambled_cube(3)))
print(mate_in_n(scrambled_cube(4)))
print(mate_in_n(scrambled_cube(5)))
print(mate_in_n(scrambled_cube(6), 6))
print(mate_in_n(scrambled_cube(7), 7))
print(mate_in_n(scrambled_cube(8), 8))