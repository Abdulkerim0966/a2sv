class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dect=defaultdict(list)
        dect1=defaultdict(list)
        for i in range(len(nums)):
            dect[nums[i]].append(i)
            dect1[nums[i]].append(i)
        arr=[0]*(len(nums))

        for num in dect:
            
            for j in range(1,len(dect[num])):
                dect[num][j]+=dect[num][j-1]
       
        for num in dect:
            if len(dect[num])>1:
                print(dect[num],dect1[num])
                for j in range(len(dect[num])):
                    if j==0:
                        temp=0
                    else:
                        temp=dect[num][j-1]
                    print((dect1[num][j]*j)-temp,(dect[num][-1]-dect[num][j])-(dect1[num][j]*(len(dect[num])-j-1)))
                    arr[dect1[num][j]]=((dect1[num][j]*j)-temp)+((dect[num][-1]-dect[num][j])-(dect1[num][j]*(len(dect[num])-j-1)))


        
        return arr

        