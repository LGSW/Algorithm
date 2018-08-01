class solution(object):
    def bubble_sort(self, nums):
        for i in range(len(nums)-1):
            for j in range(len(nums) - i -1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

a = solution()
print(a.bubble_sort([45, 32, 8, 33, 12, 22, 19, 97]))

