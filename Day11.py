QUESTION1: LARGEST ELEMENT :
class Solution:
    def largest(self, arr):
        # code here
        arr.sort()
        return arr[-1]

QUESTION2: Maximum subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxending=nums[0]
        res=nums[0]

        for i in range(1,len(nums)):
            maxending=max(maxending+nums[i],nums[i])
            res=max(res,maxending)
        return res


QUESTION 3: Task Manager

There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the TaskManager class:

TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

CODE:
import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.q=[]
        self.active={}
        for (uid,tid,p) in tasks:
            heapq.heappush(self.q,(-p,-tid,uid))
            self.active[tid]=(p,uid)
    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.q,(-priority,-taskId,userId))
        self.active[taskId]=(priority,userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.active:
            (p,u)=self.active[taskId]
            self.active[taskId]=(newPriority,u)
            heapq.heappush(self.q,(-newPriority,-taskId,u))
        
    def rmv(self, taskId: int) -> None:
        if taskId in self.active:
            del self.active[taskId]
    def execTop(self) -> int:
        while self.q:
            p,tid,uid=heapq.heappop(self.q)
            p=-p
            tid=-tid
            if tid in self.active and self.active[tid] == (p, uid):
                del self.active[tid]
                return uid
        return -1
            
        


int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.
