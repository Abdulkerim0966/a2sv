class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ma=max(nums)
        maped=[0]*ma
        for i in nums:
            maped[i-1]+=1
        totalMove=0
        toremove=0
        for i in range(len(maped)):
            if maped[i]!=0:
                break
            else:
                toremove+=1
        maped=maped[toremove:]
        
        no_changed=0
        print(maped)
        for i in range(len(maped)-1,0,-1):
            if maped[i]!=0:
                no_changed+=maped[i]
                totalMove+=no_changed
                print(no_changed,totalMove)

            
        return totalMove


        