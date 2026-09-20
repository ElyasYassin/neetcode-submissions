class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combination = []
        combinations = set()

        def dfs(i):
            if sum(combination) == target:
                combinations.add(tuple(combination))
                return

            if i >= len(candidates):
                return

            if sum(combination) > target:
                return 

            

            # include elemnt
            combination.append(candidates[i])
            dfs(i + 1)

            # don't include element
            combination.pop()
                        
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1)      

        dfs(0)
        return [list(n) for n in combinations]