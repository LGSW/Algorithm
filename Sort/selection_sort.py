class solution(object):
    def selection_sort(self,nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

x = solution()
print(x.selection_sort([4,5,3,6,2]))