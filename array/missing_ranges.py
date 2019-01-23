Description
Given a sorted integer array where the range of elements are in the inclusive
range [lower, upper], return its missing ranges.

Have you met this question in a real interview?
Example
Given nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
return ["2", "4->49", "51->74", "76->99"].


class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        res = []
        newlist = [lower-1] + nums + [upper+1]
        for i in range(len(newlist)-1):
            if newlist[i+1] - newlist[i] >= 2:
                if newlist[i+1] - newlist[i] == 2:
                    res.append(str(newlist[i]+1))
                else:
                    res.append(str(newlist[i]+1) + "->" + str(newlist[i+1]-1))

        return res
        
