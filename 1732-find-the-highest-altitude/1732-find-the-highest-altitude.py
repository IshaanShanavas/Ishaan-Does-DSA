class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # point = [0]
        # alt = 0

        # for i in gain:
        #     point.append(alt + i)
        #     alt += i
        
        # return max(point)

        max = 0
        sum = 0
        for item in gain:
            sum = sum + item
            if sum > max:
                max = sum

        return max

