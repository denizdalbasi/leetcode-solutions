class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mylist = nums1+nums2
        n = len(mylist)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if mylist[j] < mylist[min_index]:
                    min_index = j
            min_value = mylist.pop(min_index)
            mylist.insert(i, min_value)
        median=-1
        for i in range(len(mylist)):
            m = int(n/2)
            if n%2 == 0:
                median = (mylist[m] + mylist[m-1])/2
            else:
                median = mylist[m]
        return median


            

        