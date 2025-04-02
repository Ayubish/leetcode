class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(leftHalf, rightHalf):
            i, j = 0, 0,
            merged = []

            while i<len(leftHalf) and j<len(rightHalf):
                if leftHalf[i]<rightHalf[j]:
                    merged.append(leftHalf[i])
                    i += 1
                else:
                    merged.append(rightHalf[j])
                    j += 1
            merged.extend(leftHalf[i:])
            merged.extend(rightHalf[j:])
            return merged
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2

            leftHalf = mergeSort(arr[:mid])
            rightHalf = mergeSort(arr[mid:])

            return merge(leftHalf, rightHalf)
            
        return mergeSort(nums)