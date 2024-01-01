class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        arr2=sorted(arr)
        n=len(arr)-1
        def revers(poi):
            print(poi)
            for i in range(poi//2):
                arr[i],arr[poi-i-1] =arr[poi-i-1],arr[i] 
            print(arr)
        for i in range(len(arr)):
            if arr2!=arr:
                # print(arr[0:n-i])
                if i!=n and max(arr[0:n+1-i]) != arr[n-i]  :
                    s=arr.index(max(arr[0:n-i]))
                    if s+1!=1:
                        ans.append(s+1)
                    ans.append(n+1-i)
                    
                    revers(s+1)
                    revers(n+1-i)
                else:
                    continue
                # print(arr)

                    
            else:
                break
        return ans




                    

        