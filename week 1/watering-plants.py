class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count=0
        fi=capacity
        for ind, pla in enumerate (plants) :
            if fi>=pla:
                count+=1
                fi-=pla
                print(ind,pla)
            else:
                count+=2*ind +1
                fi=capacity
                fi-=pla
        return(count)
