class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx1 = 0
        idx2 = len(numbers)-1
        while(idx1<idx2):  # can also use a for-loop: for num in numbers: 
            left = numbers[idx1]
            right = numbers[idx2]
            if (left + right) < target:
                idx1 += 1
            elif (left + right) > target:
                idx2 -= 1
            else:
                return [idx1+1,idx2+1]
