import random
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def find_words(board, words):
    def backtrack(board, node, i, j, path, result):
        # If the current path is a valid word, add to the result
        if node.is_end_of_word:
            result.add(path)

        # Mark the current cell as visited
        temp, board[i][j] = board[i][j], '#'

        # Explore the 4 possible directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] != '#':
                char = board[ni][nj]
                if char in node.children:
                    backtrack(board, node.children[char], ni, nj, path + char, result)

        # Unmark the current cell as visited
        board[i][j] = temp

    # Insert all words into a Trie
    trie = Trie()
    for word in words:
        trie.insert(word)

    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            char = board[i][j]
            if char in trie.root.children:
                backtrack(board, trie.root.children[char], i, j, char, result)

    return list(result)


# Example usage
def create_board(words, size=15):
    # Initialize an empty board with placeholders (e.g., '.')
    board = [['.' for _ in range(size)] for _ in range(size)]

    def place_word(word):
        word_len = len(word)

        # Try to place the word randomly
        placed = False
        while not placed:
            direction = random.choice(['horizontal', 'vertical'])

            if direction == 'horizontal':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - word_len)

                # Check if the word fits without overlapping
                if all(board[row][col + i] == '.' for i in range(word_len)):
                    for i in range(word_len):
                        board[row][col + i] = word[i]
                    placed = True
            else:
                row = random.randint(0, size - word_len)
                col = random.randint(0, size - 1)

                # Check if the word fits without overlapping
                if all(board[row + i][col] == '.' for i in range(word_len)):
                    for i in range(word_len):
                        board[row + i][col] = word[i]
                    placed = True

    # Place all words on the board
    for word in words:
        place_word(word)

    return board


def print_board(board):
    for row in board:
        print(" ".join(row))


# List of words to place on the board
words = [
    "algorithm", "tendency", "backtracking", "greedy", "manhattan",
    "memoization", "programming", "optimization", "dynamic", "search"
]

# Create the board
board = create_board(words)

# Print the board
print_board(board)

words = [
    "algorithm", "tendency", "backtracking", "greedy", "manhattan",
    "memoization", "programming", "optimization", "dynamic", "search"
]

print(find_words(board, words))
