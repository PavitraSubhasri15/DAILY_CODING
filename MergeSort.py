QUESTION: MERGE SORT


class Solution:
 
    def mergeSort(self, arr, l, r):
        #code here
        
        def merge(arr,l,m,r):
            n1=m-l+1
            n2=r-m
            L=[]
            R=[]
            
            for i in range(n1):
                L.append(arr[l+i])
            for j in range(n2):
                R.append(arr[m+j+1])
                
            i=0
            j=0
            k=l
            while i<n1 and j<n2:
                if L[i]<R[j]:
                    arr[k]=L[i]
                    i+=1
                    k+=1
                else:
                    arr[k]=R[j]
                    j+=1
                    k+=1
            while i<n1:
                arr[k]=L[i]
                i+=1
                k+=1
            while j<n2:
                arr[k]=R[j]
                j+=1
                k+=1
        if l<r:
            m=l+(r-l)//2
            self.mergeSort(arr,l,m)
            self.mergeSort(arr,m+1,r)
            merge(arr,l,m,r)
        
        
                
