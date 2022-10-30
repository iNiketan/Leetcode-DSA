class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brut force solution
        for i in range(len(nums)):
            c = target-nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == c:
                    return i, j
                  #On2 complexity
           
                    
                    
      # hash map solution              
      d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
               #On complexity
 #https://www.youtube.com/watch?v=KLlXCFG5TnA  solution explation
                    
                    
                    
                    
                    
                    
                    
                    
                    
         
