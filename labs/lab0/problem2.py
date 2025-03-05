import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

def count_mines(i, j, n, table):
    count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if 0 <= i + x < n and 0 <= j + y < n and table[i + x][j + y] == '#':
                count += 1
    return count


if __name__ == "__main__":
    n=int(input())
    table=[input().split() for _ in range(n)]

    
    "sol=[ for i in range(n) for j in range(n) str(count_mines(i, j, n, table) if table[i][j] == '-' else '#')]" 
    sol=[
        [
            str(count_mines(i, j, n, table) if table[i][j] == '-' else '#')
            for j in range(n)
        ]
        for i in range(n)
    ]
    for each in sol:
        print("   ".join(each))