class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum=[]
        sum.append (0)
        tsum=0
        su=0
        for i in range (len(arr)):
            tsum+=arr[i]
            sum.append (tsum)
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if (j-i)%2==0:
                    su+=sum[j+1]-sum[i]
        return su