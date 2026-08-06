class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # my_set = set(nums)
        return len(set(nums)) != len(nums)
        