def part1():
    with open("input.txt") as f:
        grid = [list(line.rstrip("\n")) for line in f]

    H = len(grid)
    W = len(grid[0])

    p1_count = 0

    for r in range(H):
        for c in range(W):
            if grid[r][c] != '@':
                continue

            neighbours = 0
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < H and 0 <= nc < W:
                        if grid[nr][nc] == '@':
                            neighbours += 1

            if neighbours < 4:
                p1_count += 1

    print(p1_count)


def part2():
    with open("input.txt") as f:
        grid = [list(line.rstrip("\n")) for line in f]

    H = len(grid)
    W = len(grid[0])

    p2_count = 0

    while True:
        to_remove = []

        for r in range(H):
            for c in range(W):
                if grid[r][c] != '@':
                    continue

                neighbours = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < H and 0 <= nc < W:
                            if grid[nr][nc] == '@':
                                neighbours += 1

                if neighbours < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        p2_count += len(to_remove)

    print(p2_count)


part1() #1367
part2() #9144
