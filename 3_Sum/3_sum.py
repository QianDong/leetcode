class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        nums.sort()     # always important to sort
        for left_idx in list(range(0,len(nums))):
            if left_idx > 0 and nums[left_idx] == nums[left_idx-1]: # in case of replicated values
                continue     # do nothing, until find the one that is not replicated
            middle_idx = left_idx+1
            right_idx = len(nums) - 1
            while middle_idx < right_idx :
                threesum = nums[left_idx] + nums[middle_idx] + nums[right_idx]
                if threesum < 0:   #then middle should be larger
                    middle_idx += 1
                    print("<0", middle_idx)
                elif threesum > 0:   #then right should be smaller                   
                    right_idx -= 1
                    print(">0", middle_idx)
                else:     # else sum == 0
                    res.append([nums[left_idx],nums[middle_idx],nums[right_idx]])
                    middle_idx += 1
                    while middle_idx < right_idx and nums[middle_idx] == nums[middle_idx-1]:  #filter out all the repeatitive-values
                        middle_idx += 1                    
        return res
            
                
mySolution = Solution()
result = mySolution.threeSum([-1,0,1,2,-1,-4])
print(result)
