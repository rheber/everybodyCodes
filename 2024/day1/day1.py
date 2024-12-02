from typing import List, Tuple
from itertools import islice

# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
def chunk(arr_range, arr_size):
    arr_range = iter(arr_range)
    return iter(lambda: tuple(islice(arr_range, arr_size)), ())

def potionsNeeded(letter: str) -> int:
    if (letter == 'C'):
        return 3
    if (letter == 'B'):
        return 1
    if (letter == 'D'):
        return 5
    return 0

def potionsNeededBattle(battle: Tuple[str, str]) -> int:
    L,R = battle
    return potionsNeeded(L) + potionsNeeded(R) + (2 if L != 'x' and R != 'x' else 0)

def potionsNeededTrip(battle: Tuple[str, str, str]) -> int:
    L,M,R = battle
    def adjustment():
        if L != 'x' and M != 'x' and R != 'x':
            return 6
        if sum(map(lambda let: let == 'x', list(battle))) == 1:
            return 2
        return 0
    return potionsNeeded(L) + potionsNeeded(M) + potionsNeeded(R) + adjustment()

def pairs(line: str) -> List[Tuple[str, str]]:
    return chunk(line, 2)

def part1() -> int:
    with open("./input.txt") as f:
        line: str = f.read()
        return sum(map(potionsNeeded, line))

def part2() -> int:
    with open("./input2.txt") as f:
        line: str = f.read()
        battles = pairs(line)
        return sum(map(potionsNeededBattle, battles))

def part3() -> int:
    with open("./input3.txt") as f:
        line: str = f.read()
        battles = chunk(line, 3)
        return sum(map(potionsNeededTrip, battles))

print(part3())