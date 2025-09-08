QUESTION: Bubble sort

class Solution:
    def bubbleSort(self,arr):
        # code here
        for i in range(len(arr)):
            swapped=False
            for j in range(len(arr)-1,0,-1):
                if arr[j]<arr[j-1]:
                    swapped=True
                    arr[j],arr[j-1]=arr[j-1],arr[j]
            if not swapped:
                break
        return arr
                
