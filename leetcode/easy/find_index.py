class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            haystack = haystack.split(needle)
            return len(haystack[0])
        else:
            return -1
        
        # if len(needle) > len(haystack):
        #     return -1
        
        # left = 0
        # right = 0
        # index = 0

        # while right < len(haystack):
        #     if haystack[right] == needle[index]:

        #         index += 1
        #         if index == len(needle):
        #             return left
        #         right += 1
        #     else:
        #         right += 1
        #         left = right
        #         index = 0
        # return -1