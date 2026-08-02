class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for char in s:
            if char.islower():
                result += char

            elif char == '*':
                if result:
                    result = result[:-1]
                else:
                    continue

            elif char == '#':
                result = result * 2

            elif char == '%':
                result = result[::-1]

            else:
                continue
        
        return result