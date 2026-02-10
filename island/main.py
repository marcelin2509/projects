# can you count how many "islands" are there in this matrix ?
# island: a 1 surrounded by 0 all around.

mat_A = [
#  0  1  2  3  4  5  6
  [0, 0, 1, 1, 1, 0, 0], # 0
  [1, 1, 0, 0, 1, 1, 1], # 1
  [0, 0, 0, 0, 0, 0, 0], # 2
  [0, 0, 1, 0, 0, 0, 1], # 3
  [1, 0, 0, 0, 1, 0, 0], # 4
  [1, 0, 1, 1, 0, 0, 0], # 5
  [0, 1, 1, 0, 1, 0, 1], # 6
]
  
def count_islands(mat: list[list[int]]) -> int:
    count = 0
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] != 1:
                continue
            
            is_island = True
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if i == r and j == c:
                        continue

                    if 0 <= i < len(mat) and 0 <= j < len(mat[r]) and mat[i][j] == 1:
                        is_island = False
                        break

                if not is_island:
                    break

            if is_island:
                count += 1

    return count

island_count = count_islands(mat_A)
print("Island Count:", island_count)
assert(island_count == 3)
