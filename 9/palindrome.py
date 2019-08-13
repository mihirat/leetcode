import copy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = [s for s in str(x)]
        arr_rev = copy.copy(arr)
        arr_rev.reverse()
        if arr == arr_rev:
            return True
        return False
    