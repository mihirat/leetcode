class Solution:

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        is_minus = False
        if x < 0:
            x *= -1
            is_minus = True

        arr = [s for s in str(x)]
        arr.reverse()

        for i in range(0, len(arr)):
            max_zero_cnt = 0
            if arr[i] == '0':
                max_zero_cnt += 1
            else:
                break
        if max_zero_cnt > 0:
            del(arr[:max_zero_cnt])

        res = int("".join(arr))
        if is_minus:
            res *= -1
        if res <= (-2)**31 or res >= 2**31 - 1:
            return 0
        return res
