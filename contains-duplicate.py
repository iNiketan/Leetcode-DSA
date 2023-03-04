# que_link: https://leetcode.com/problems/contains-duplicate-ii/description/

def containsDuplicate(nums):
    #Creating a data structure to store each element in array we scan through
    hash_table = {}
    #Going through each element in array
    for p in range(len(nums)):
        #If the current element is not in a data structure we created yet then append current element else we know that array is duplicated
        if hash_table.get(nums[p]):
            print(hash_table)
            return True
        else:
            hash_table[nums[p]] = True
    return False

# input 
nums = [1,2,3,5,1]
containsDuplicate(nums)

