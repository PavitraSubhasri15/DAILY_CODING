class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for num in nums:
            if count==0:
                candidate,count=num,1
            elif candidate==num:
                count+=1
            else:
                count-=1
        if nums.count(candidate)>n//2:
            return candidate
        return -1


