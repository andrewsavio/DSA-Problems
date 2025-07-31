class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        missing = -1
        repeating = -1

        for i in range(n):
            index = abs(arr[i])-1
            if arr[index] < 0:
                repeating = abs(arr[i])
            else:
                arr[index] = -arr[index]

        for i in range(n):
            if arr[i] > 0:
                missing = i+1
                break
        return [repeating, missing]
