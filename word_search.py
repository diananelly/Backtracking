class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the word if the path completes a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Mark end of word


def find_words_in_grid(grid, words):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    result = set()

    # Build Trie for fast lookups
    trie = Trie()
    for word in words:
        trie.insert(word)

    def backtrack(x, y, node):
        char = grid[x][y]
        if char not in node.children:
            return  # If character not in Trie, stop searching

        next_node = node.children[char]
        if next_node.word:
            result.add(next_node.word)  # Found a word
            next_node.word = None  # Avoid duplicate finds

        # Mark the cell as visited
        grid[x][y] = "#"

        # Explore all directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] in next_node.children:
                backtrack(nx, ny, next_node)

        # Restore the cell after backtracking
        grid[x][y] = char

        # Optimization: Remove leaf nodes in Trie for efficiency
        if not next_node.children:
            del node.children[char]

    # Start backtracking from all positions
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in trie.root.children:  # Start only if first letter exists
                backtrack(i, j, trie.root)

    return list(result)


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

