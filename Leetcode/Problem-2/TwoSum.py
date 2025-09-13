class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = list(map(int, input("Enter nums list = ").split(',')))
        # target = int(input("Enter target = "))
        result = []
        numsCopy = nums.copy()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:                   
                    result.append(nums.index(numsCopy[i]))
                    nums[nums.index(numsCopy[i])] = 'a'
                    result.append(nums.index(numsCopy[j]))              
                    # print(first, second, nums)
                    # result.append(first)
                    # result.append(second)
                    return result
        # print("Exited")
        
        