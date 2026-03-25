arr = [1, 1, 2]


def remove_duplicates(nums: list[int]) -> int:
    """
        this function takes an array of numbers and using "two pointer" method one pointer points at the write index,
        starting at 1 as the first item is always unique, we loop through the nums using a read index and compare the
        read index with the number proceeding it, if they are not the same we overwrite the write index with the number
        in the current read index, then increment the write index
    """
    write_index = 1

    for read_index in range(1, len(nums)):

        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index


print(remove_duplicates(nums=arr))


def contains_duplicate(nums: list[int]) -> bool:
    """
        this function takes an array of numbers and checks for duplicates, comparing the length of the list to a set
        conversion from the list (sets don't allow dupes) if they are the same there are no duplicates
    """
    if len(set(nums)) != len(nums):
        return True
    else:
        return False


print(contains_duplicate(nums=[1, 2, 3, 4, 1]))


def two_sum(nums: list[int], target: int) -> list[int]:
    """
     this algorithm takes a list of numbers and creates a hash table of indexes and numbers
     we then loop through the table looking for the required target, the required target is the remainder of the
     current item in the hash table subtracted from the target.
     we then get the key from the hash table of the value thats equal to the required_target value but not the same as
     x which is the index we are currently on to avoid returning the same index for nums = [3,3] target = 6

    """
    hash_table = {}
    for num in range(0, len(nums)):
        hash_table[num] = nums[num]
        print(hash_table)

        for x, y in hash_table.items():
            required_value = target - y
            key = [key for key, value in hash_table.items() if value == required_value and key != x]

            if len(key) > 0:
                return [x, key[0]]


print(two_sum(nums=[1, 2, 3, 2, 5], target=8))


def isBadVersion(version: int):
    """
    required mock version of the bad version endpoint to check if a version was bad
    """
    if version >= 5:
        return True
    else:
        return False


def firstBadVersion(n: int) -> int:
    """
        a binary search implementation for finding the first bad version based on the current version n which
        has been reported as bad
    """
    low: int = 0
    high = n

    while low <= high:

        mid = (low + high) // 2

        guess = isBadVersion(mid)

        if not isBadVersion(mid - 1) and guess:
            return mid

        if guess:
            high = mid - 1

        elif not guess:
            low = mid + 1
    return 0


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
        merge two sorted arrays, two integers m and n, representing the number of elements in nums1 and nums2
        respectively
    """
    if m == n or n > 0:
        for num in range(0, len(nums1)):
            if nums1[num] == 0:
                if len(nums2) > 0:
                    item_from_nums2 = nums2.pop(0)
                    nums1[num] = item_from_nums2
    nums1.sort()


def rotate(nums: list[int], k: int) -> None:
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    """
    for i in range(0, k):
        item = nums.pop(len(nums) - 1)
        nums.insert(0, item)


def singleNumber(nums: list[int]) -> int:
    """
        this method finds the only single number in an array containing duplicates all bar one number
    """
    for num in nums:
        count = nums.count(num)
        if count == 1:
            return num


def moveZeroes(nums: list[int]) -> None:
    """
     using two pointer techniques we move all th 0's to the end of the nums list
    """
    slow = 0
    for fast in range(0, len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

