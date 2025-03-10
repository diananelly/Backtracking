def word_segmentation(s, word_dict):
    def backtrack(start, path, results):
        if start == len(s):  # Base case: reached the end of the string
            results.append(" ".join(path))
            return
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_dict:
                backtrack(end, path + [word], results)

    results = []
    backtrack(0, [], results)
    return results

# Example usage
s = "ilikeleetcode"
word_dict = {"i", "like", "leet", "code", "leetcode"}
print(word_segmentation(s, word_dict))
