class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        

        max = 0
        sum = 0
        for item in gain:
            sum = sum + item
            if sum > max:
                max = sum

        return max

