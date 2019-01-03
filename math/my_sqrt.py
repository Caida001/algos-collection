def mySqrt(x):
    if x == 0 or x == 1:
        return x
    else:
        start, end = 0, x
        res = 0
        while start <= end:
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start += 1
                res = mid
            else:
                end -= 1
                res = mid
        return res
