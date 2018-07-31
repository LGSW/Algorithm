class solution(object):
    nums = [5,3,2,4]

    def quicksort(self,nums,left,right):
        if left >= right:
            return
        i = left; j = right
        a = nums[left]
        while(i!=j):
            while (nums[j] >= a and i < j):
                j -= 1
            while (nums[i] <= a and i < j):
                i += 1
            if(i<j):
                nums[i], nums[j] = nums[j], nums[i]

        nums[left] = nums[i]
        nums[i] = a
        self.quicksort(nums,left,i-1)
        self.quicksort(nums,i+1,right)



a = solution()
print(a.nums)
a.quicksort(a.nums,0,3)
print(a.nums)
