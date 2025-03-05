def find_words_in_grid(grid, words):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    result = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def backtrack(x, y, word, index, visited):
        # If we reach the length of the word, we've found it
        if index == len(word):
            return True

        # Mark the current cell as visited
        visited.add((x, y))

        # Try all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == word[index]:
                if backtrack(nx, ny, word, index + 1, visited):
                    return True

        # Backtrack (unmark the current cell)
        visited.remove((x, y))
        return False

    # For each word, try to find it starting from each cell in the grid
    for word in words:
        found = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == word[0]:  # Only start if the first letter matches
                    visited = set()
                    if backtrack(i, j, word, 1, visited):
                        result.append(word)  # Word found
                        found = True
                        break
            if found:
                break

    return result

# Sample 15x15 grid
grid = [
    ["a", "l", "g", "o", "r", "i", "t", "h", "m", "q", "w", "e", "r", "t", "y"],
    ["s", "d", "t", "e", "n", "d", "e", "n", "c", "y", "r", "s", "s", "h", "b"],
    ["r", "e", "p", "b", "a", "c", "k", "t", "r", "a", "c", "k", "i", "n", "g"],
    ["p", "y", "d", "e", "e", "r", "g", "s", "t", "a", "r", "l", "f", "o", "o"],
    ["m", "a", "n", "h", "a", "t", "t", "a", "n", "n", "h", "j", "v", "c", "x"],
    ["m", "e", "m", "o", "i", "z", "a", "t", "i", "o", "n", "h", "b", "n", "k"],
    ["p", "r", "o", "g", "r", "a", "m", "m", "i", "n", "g", "a", "v", "d", "y"],
    ["o", "p", "t", "i", "m", "i", "z", "a", "t", "i", "o", "n", "u", "s", "v"],
    ["d", "n", "n", "a", "m", "i", "c", "r", "u", "p", "w", "a", "b", "h", "a"],
    ["s", "i", "p", "r", "c", "h", "g", "b", "d", "e", "t", "e", "o", "p", "c"],
    ["e", "c", "r", "t", "o", "u", "y", "g", "s", "v", "b", "h", "n", "m", "i"],
    ["a", "d", "f", "a", "d", "b", "w", "z", "y", "t", "l", "v", "f", "k", "m"],
    ["r", "g", "w", "r", "e", "r", "u", "s", "t", "p", "v", "q", "h", "c", "a"],
    ["c", "n", "m", "r", "l", "a", "z", "w", "q", "m", "a", "g", "d", "y", "n"],
    ["h", "k", "e", "l", "v", "m", "h", "r", "c", "w", "s", "t", "a", "v", "y"],
    ["v", "p", "o", "g", "l", "d", "w", "c", "o", "p", "r", "m", "s", "e", "d"]
]

words = [
    "algorithm", "tendency", "backtracking", "greedy", "manhattan",
    "memoization", "programming", "optimization", "dynamic", "search"
]

# Finding words in the grid
found_words = find_words_in_grid(grid, words)
print(found_words)
