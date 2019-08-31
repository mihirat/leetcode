class Solution:
    def isRepeating(self, s: str) -> bool:
        for str in s:
            s_rest = list(s)
            s_rest.remove(str)
            if str in s_rest:
                return True
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        start = 0
        i = 1
        while i <= len(s):
            cur = s[start:i]
            if len(cur) <= res:
                i = i + 1
                continue
            if self.isRepeating(cur):
                start = start + 1
                i = i - 1
                continue
            res = len(cur)
            i = i + 1
        return res


if __name__ == "__main__":
    res = Solution().lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ")
    print(res)
