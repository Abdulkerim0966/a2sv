class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mountain=False
        if len(arr)<2:
            return False
        for i in range(1,len(arr)):
            if  mountain==False :
                if arr[i-1]==arr[i]:
                    return False
                elif i==1 and arr[i-1]>arr[i] :
                    return False
                elif i==len(arr)-1 and arr[i-1]<arr[i]:
                    return False
                elif arr[i-1]>arr[i]:
                    mountain=True
            else:
                if arr[i-1]==arr[i]:
                    return False
                elif arr[i]>arr[i-1]:
                    return False
        return True


        