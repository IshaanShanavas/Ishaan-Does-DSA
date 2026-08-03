class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        

        point = [0]
        alt = 0

        for i in gain:
            point.append(alt + i)
            alt += i
        
        return max(point)

