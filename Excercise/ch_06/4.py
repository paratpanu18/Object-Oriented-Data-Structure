def diff(sour: int, bitter: int) -> int:
    return abs(sour - bitter)

def find(length: int, sour: int, bitter: int, sour_l: list, bitter_l: list, length_inp: int, best: int) -> int:
    if length == length_inp:
        if bitter > 0:
            return min(best, diff(sour, bitter))
        return best
    else:
        # Including the current ingredient
        best_with = find(length + 1, sour * sour_l[length], bitter + bitter_l[length], sour_l, bitter_l, length_inp, best)

        # Excluding the current ingredient
        best_without = find(length + 1, sour, bitter, sour_l, bitter_l, length_inp, best)
        return min(best_with, best_without)


inp = input("Enter Input : ").split(",")
sour_l = []
bitter_l = []

for i in inp:
    sour, bitter = map(int, i.split())
    sour_l.append(sour)
    bitter_l.append(bitter)

length_inp = len(inp)
best = find(0, 1, 0, sour_l, bitter_l, length_inp, 1_000_000_000)

print(best)
