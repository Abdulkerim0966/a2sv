class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.per=[]
        self.per.append(persons[0])
        dect=Counter()
        dect[persons[0]]+=1
        curr=persons[0]

        for i in range(1,len(persons)):
            dect[persons[i]]+=1
         
            if dect[curr]>dect[persons[i]]:

                self.per.append(curr)
            else:
                self.per.append(persons[i])
                curr=persons[i]
        
        self.time=times

     

    def q(self, t: int) -> int:

     
        idx=bisect_right(self.time,t)-1
        
        return self.per[idx]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)