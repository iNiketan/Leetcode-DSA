class Solution(object):
    def twoSum(self, nums, target):
        # brut force solution
        for i in range(len(nums)):
            c = target-nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == c:
                    return i, j
                  #On2 complexity
           
                    
                    
    # hash map solution   
    def twoSum(self, nums, target):
        hashmap = {}
        # populate the hash map
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            # checking if complement exist in hmap
            # if it does check index is diff 
            # eg: [3,3] {3:0, 3:1}
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]           
      
    #O(n) complexity
 #https://www.youtube.com/watch?v=KLlXCFG5TnA  solution explation
                    
                    
                    
                    
                    
                    
                    
                    
         
