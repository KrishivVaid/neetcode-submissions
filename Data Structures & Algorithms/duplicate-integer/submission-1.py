class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        heapset=set()
        for i in nums:
            if i in heapset:
                return True
            heapset.add(i)
        return False
        