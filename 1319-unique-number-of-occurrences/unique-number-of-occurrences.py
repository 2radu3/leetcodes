class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arrSet = Counter(arr)

        return len(set(arrSet.values())) == len(arrSet)