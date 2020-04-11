class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        def max_array(arr, n):
            stack = []
            for i, e in enumerate(arr):
                while stack and stack[-1] <e:
                    if len(stack) + len(arr) - i >n:
                        stack.pop()
                    else:
                        break
                if len(stack)<n:
                    stack.append(e)
            return stack
        def merge(arr1, arr2):
            if not arr1 or not arr2:
                return arr1 + arr2
            ret = []
            m , n = len(arr1), len(arr2)
            i, j = 0,0
            arr1 += [-1]
            arr2 += [-1]
            while i <m or j < n:
                if arr1[i] > arr2[j]:
                    ret.append(arr1[i])
                    i+=1
                elif arr1[i] < arr2[j]:
                    ret.append(arr2[j])
                    j+=1
                else:
                    if arr1[i:] > arr2[j:]:
                        ret.append(arr1[i])
                        i += 1
                    else:
                        ret.append(arr1[i])
                        j+=1
            return ret
        m , n = len(nums1), len(nums2)
        ret = []
        for i in range(max(k - n, 0), min(k, m)+1):
            ret = max(ret, merge( max_array(nums1, i), max_array(nums2, k - i) ))

        return ret
        #return max(merge(max_array(nums1,i), max_array(nums2,k-i)) for i in range(max(k-n,0), min(k,m)))

"""
def merge(a, b):
        return [max(a, b).pop(0) for _ in a+b]

"""


sol = Solution()

nums1 = [3,4,6]
nums2 = [9,1]
k = 5

print(sol.maxNumber(nums1, nums2, k))
