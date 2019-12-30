class Solution:
    def candy(self, ratings) -> int:
        #점수가 같아도 옆에서 조금 받기 가능
        #합을 내리막길로 생각? 오르막길로 생각!
        m = len(ratings)
        if m == 1:
            return 1
        start = 0
        end = 1
        ret = [0]*m
        while end<m:#ascending
            #plat
            if ratings[start] == ratings[end]:
                while end < m-1 and ratings[end] == ratings[end + 1]:
                    end +=1
                for i in range(start+1, end +1):
                    ret[i] = 1
                if ret[start] <2:
                    ret[start] = 1
            #ascending
            elif ratings[start] < ratings[end]:
                while end < m-1 and ratings[end] < ratings[end+1]:
                    end +=1
                for i in range(start,end + 1):
                    ret[i] = i - start + 1
            # descending
            elif ratings[start] > ratings[end]:
                while end < m-1 and ratings[end] > ratings[end + 1]:
                    end +=1
                for i in range(end,start,-1):
                    ret[i] = end - i + 1
                if ret[start] < end - start + 1:
                    ret[start] = end - start + 1
            start = end
            end +=1
        sum = 0
        for i in ret:
            sum += i
        return sum
sol = Solution()
ratings = [1,0,2]
print(sol.candy(ratings))