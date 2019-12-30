class Solution:
    def trap(self, heights) -> int:
        ret = 0
        #연속된 하강 이후 처음 만나는 하강하는 블록
        #find left, find right
        i = 0
        if len(heights)<3:
            return 0

        while i < len(heights) - 2:
            if heights[i] > heights[i + 1]:
                left = i
                j = i+1

                cur_rain = 0
                next_rain = 0
                max = 0
                accent = False
                while j<len(heights):
                    hj = heights[j]
                    if hj>=max and hj < heights[left]:
                        max = hj
                        cur_rain += next_rain
                        next_rain = 0
                        right = j
                    elif hj >=  heights[left]:
                        right = j
                        cur_rain += next_rain
                        break
                    if hj>heights[j-1]:
                        accent = True

                    next_rain += hj
                    j += 1

                ret += (right - left - 1) * min(heights[right], heights[left]) - cur_rain
                if j == len(heights):

                    if not accent:
                        return ret
                i = right
            else:
                i += 1
        return ret

heights= [0,1,0,2,1,0,1,3,2,1,2,1]
sol =Solution()
print(sol.trap(heights))