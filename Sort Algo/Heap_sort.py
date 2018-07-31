class solution(object):
    nums = [4,5,3,6,2,1]

    def heap_sort(self,nums):
        l = len(nums)
        for i in range(0 ,l//2)[::-1]:
            self.heapAdjust(nums, i, l-1);
        while l >= 1:
            nums[0],nums[l-1] = nums[l-1], nums[0]
            l -= 1
            self.heapAdjust(nums, 0, l-1)

    def heapAdjust(self, nums, low, high):
        temp = nums[low]
        i = low
        j = 2 * i + 1
        while j <= high:
            if j < high and nums[j] < nums[j+1]:
                j += 1
            if temp < nums[j]:
                nums[i] = nums[j]
                i = j
                j = 2 * i + 1
            else:
                break
        nums[i] = temp

case = solution()
case.heap_sort(case.nums)
print(case.nums)




