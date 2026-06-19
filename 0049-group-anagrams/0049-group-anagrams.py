from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # group = {}

        # for s in strs:
            
        #     hash = Counter(s)
        #     print(hash)
        #     sort_hash = dict(sorted(hash.items(), key = lambda x: x[0]))
        #     ana = ""
        #     for u, v in sort_hash.items():
        #         ana += (str(u) + str(v))
            
        #     if ana in group:
        #         group[ana].append(s)
        #     else:
        #         group[ana] = [s]
        
        # return [value for key, value in group.items()]

        group = {}

        for s in strs:
            ss = str(sorted(s))
            if ss in group:
                group[ss].append(s)
            else:
                group[ss] = [s]
        
        return [value for key, value in group.items()]