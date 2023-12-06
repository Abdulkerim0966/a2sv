class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        no1=0
        no2=0
        
        i2=0

        while no2!=n:

            if no1==m+i2:

                nums1[m+i2] = nums2[no2]
                no2+=1
                i2+=1
            elif nums1[no1]<=nums2[no2]:
                no1+=1
            elif nums1[no1]>nums2[no2]:
                nums1.insert(no1,nums2[no2])
                nums1.pop(len(nums1)-1)
                no2+=1
                no1+=1
                i2+=1
         
        

            
       
        
        