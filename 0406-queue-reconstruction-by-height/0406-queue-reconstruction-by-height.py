class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key = lambda p : (-p[0], p[1]))
        
        ans = []

        for person in people:
            ans.append(person)

            i = len(ans)-1

            while i > person[1]:
                ans[i] = ans[i-1]
                i -= 1
            
            ans[i] = person
        
        return ans