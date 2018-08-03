# Binary Search Algorithm

def binary_search(nums, target):
    low = 0; high = len(nums) - 1
    while(low < high):
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

x = [1,2,4,7,9,13]
print(binary_search(x, 4))
print(binary_search(x, 5))



