class Solution(object):
    def concatenatedBinary(self,n):
        """
        :type n: int
        :rtype: int
        """
        concat_str = ''
        for i in range(n+1):
            binary_i = bin(i)[2:] # convert to binary number and remove the "0b" head 
            concat_str = concat_str + binary_i
        decimal_number = int(concat_str,2) # convert binary to decimal, set base of 2 for binary  
        
        modulo_number = 1000000007
        return decimal_number % modulo_number
