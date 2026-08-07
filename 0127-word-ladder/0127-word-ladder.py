from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord, 1))

        while queue:

            word, length = queue.popleft()

            if word == endWord:
                return length

            word_chars = list(word)

            for i in range(len(word_chars)):
                original = word_chars[i]

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    word_chars[i] = ch
                    newWord = "".join(word_chars)

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, length + 1))

                word_chars[i] = original

        return 0