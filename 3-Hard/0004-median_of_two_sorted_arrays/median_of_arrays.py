class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mylist = sorted(nums1+nums2)
        n=len(mylist)
        for i in range(n):
            m = int(len(mylist)/2)
            if n%2 == 0:
                median = (mylist[m] + mylist[m-1])/2
            else:
                median = mylist[m]
        return median


            

        