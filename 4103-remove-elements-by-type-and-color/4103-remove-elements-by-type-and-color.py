class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:

        # n = len(types)
        # for g in groupSize:
        #     found = False

        #     for i in range(n - g + 1):
        #         if (all(x == types[i] for x in types[i:i+g]) and
        #             all(x == colors[i] for x in colors[i:i+g])):

        #             del types[i:i+g]
        #             del colors[i:i+g]

        #             n -= g
        #             found = True
        #             break

        #     if not found:
        #         return False

        # return len(types) == 0

        stack = []

        for t, c in zip(types, colors):

            if stack and stack[-1][0] == t and stack[-1][1] == c:
                stack[-1][2] += 1
            else:
                stack.append([t, c, 1])

            if stack[-1][2] == groupSize[t]:
                stack.pop()

        return len(stack) == 0