class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ma=0
        print(tasks)
        for i in range(len(processorTime)):
            if tasks[4*i]+processorTime[i]>ma:
                ma=tasks[4*i]+processorTime[i]
        return ma


    
        


        