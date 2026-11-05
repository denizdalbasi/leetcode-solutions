class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        size1 = (len(arr1))
        size2=(len(arr2))
        count=0
        for i in range (size1):
            for j in range (size2):
                arra = []
                dis = abs(arr1[i] - arr2[j])
                if(dis<=d):
                    arra = [0] * size2
                    break
                
                arra.append(dis)
                
            minimum = min(arra)
            if(minimum > d): 
                count += 1
            
        return count

