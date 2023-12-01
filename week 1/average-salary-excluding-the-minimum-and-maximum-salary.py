class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        s=sum(salary)
        return s/len(salary)
        