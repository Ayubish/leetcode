"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        servants = {e.id: e for e in employees}
        
        def dfs(eid):
            servant = servants[eid]
            total = servant.importance

            for sub in servant.subordinates:
                total += dfs(sub)
            return total

        return dfs(id)