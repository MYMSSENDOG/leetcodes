class Solution:
    def sortColors(self, nums) -> None:
        n0, n1, n2 = 0,0,0
        for i in nums:
            if i == 0:
                n0 +=1
            elif i == 1:
                n1 +=1
            elif i == 2:
                n2 +=1
        for i in range(0,n0):
            nums[i] = 0
        for i in range(n0,n1+n0):
            nums[i] = 1
        for i in range(n1+n0,n2+n1+n0):
            nums[i] = 2
        print(nums)
#dutch partitioning
# 0 1 2의 그룹으로 나누고 2면 2만 추가 1이면 1하나 늘리고 2하나 늘림 0이면 0하나 1 하나 2 하나 늘림
#0 -> [0:i) -> [0:i+1)  1-> [i:j) -> [i+1:j+1) 2-> [j:k)-> [j+1:k+1)
sol = Solution()
Input =  [2,0,2,1,1,0]
print(sol.sortColors(Input))