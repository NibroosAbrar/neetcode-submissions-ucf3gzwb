class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        maps = {}

        for i, n in enumerate(numbers):
            complement = target - numbers[i]
            if complement in maps:
                return [maps[complement]+1, i+1]
            maps[n]= i
        