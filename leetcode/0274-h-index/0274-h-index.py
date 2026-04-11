class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)

        h = 0
        count = 0

        for cited in citations:
            count += 1
            if cited >= h and cited >= count:
                h += 1
            else:
                break
        return h