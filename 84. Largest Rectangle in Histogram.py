class Solution:
    def largestRectangleArea(self, heights) -> int:
#범위가 있고 그범위에서 가장 작은값 * 범위
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

sol = Solution()
heights = [1,4,8,3,2]
print(sol.largestRectangleArea(heights))