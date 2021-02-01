class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        charX = str(x)   # charX= '86345'
        reverse_list = []
        if x>=0:
            for idx in list(range(1,len(charX)+1)):  # [1,2,3,4,5]
                reverse_list.append(charX[-idx])  # reverse_list = ['5','4','3','6','8']
            reverse = ''.join(reverse_list)  # '54368'
            if int(reverse) <= 2**31:
                return int(reverse)
            else:
                return 0
        else:
            for idx in list(range(1,len(charX))):
                reverse_list.append(charX[-idx])
            reverse = ''.join(reverse_list)
            if int(reverse) >= -2**31:
                return -int(reverse)
            else:
                return 0
        
mySolution = Solution()
res = mySolution.reverse(1563847412)
print(res)
