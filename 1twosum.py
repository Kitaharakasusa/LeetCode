class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin=0
        end=1
        ans=[]
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    ans.append(i)
                    ans.append(j)
                    return ans
    def sum(self,nums,target):
        begin=0
        end=len(nums)-1
        ans=[]
        while(True):
            sum1=nums[begin]+nums[end]
            if sum1==target:
                ans.append(begin)
                ans.append(end)
                return ans
            elif sum1<target:
                begin+=1
            elif sum1>target:
                end-=1
    def sum2(self,nums,target):
        recoder={}
        ans=[]
        for i in range(0,len(nums)):
            index=recoder.get(target-nums[i])
            if index==None:
                recoder[nums[i]]=i
            else:
                ans.append(i)
                ans.append(index)
                ans.sort()
                return ans

if __name__=="__main__":
    nums = [-1,-2,-3,-4,-5]
    target = -8
    sol=Solution()
    ans=sol.sum2(nums,target)
    print(ans)
