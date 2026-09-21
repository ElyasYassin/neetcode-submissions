class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = stones.copy()
        res.sort()

        while len(res) > 1:
            if res[-1] == res[-2]:
                # if thw two biggest stones are the same weight then we remove both 
                # edge case: if last two remaining stones then we want to add a 0 element
                if len(res) == 2:
                    return 0
                res.pop()
                res.pop()
            
            elif res[-1] < res[-2]:
                tmp = res[-2] - res[-1]
                res.pop()
                res.pop()
                res.append(tmp)
            
            else:
                tmp = res[-1] - res[-2]
                res.pop()
                res.pop()
                res.append(tmp)
            
            res.sort()
        
        return res[0]
        