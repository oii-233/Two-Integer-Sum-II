class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length=len(numbers)
        left=0
        right=length-1
        adi=[]
        
        while left < right:
            total=numbers[left]+numbers[right]
            if total==target:
                adi.append(left+1)
                adi.append(right+1)
                break
            elif total>target:
                right-=1
            else:
                left+=1
                
        return adi
