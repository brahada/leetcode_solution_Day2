class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for n in nums:
            if(n!=0):
                nums[j]=n
                j+=1
        for x in range(j,len(nums)):
            nums[x]=0
            
