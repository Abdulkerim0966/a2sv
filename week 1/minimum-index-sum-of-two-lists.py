class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ma=float("inf")
        id_least=[]
        for i in range (len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if i+j<ma:
                        ma=i+j
                        id_least.clear()
                        id_least.append(i)
                    elif i+j==ma:
                        id_least.append(i)
        ans=[list1[i]  for i in id_least]


        return ans