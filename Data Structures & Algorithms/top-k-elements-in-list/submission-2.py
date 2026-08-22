class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}

        for i in nums:
            if groups.get(i) is None:
                groups[i] = groups.get(i, 0) + 1
            else:
                groups[i] = groups[i]+1

        sortedHash = dict(sorted(groups.items(), key=lambda item: item[1], reverse=True))
        sortedValues = list(sortedHash.keys())

        return sortedValues[:k]