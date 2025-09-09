QUESTION:SelectionSort.py

class Solution: 
    def selectionSort(self, arr):
        #code here
        
        for j in range(len(arr)):
            minIndex=j
            for i in range(j+1,len(arr)):
                if arr[minIndex]>arr[i]:
                    minIndex=i
            arr[minIndex],arr[j]=arr[j],arr[minIndex]
        return arr
                
