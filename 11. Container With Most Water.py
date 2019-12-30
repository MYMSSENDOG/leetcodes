height = [2,3,4,5,18,17,6] # 28  97 7 * 15 / 2
#넓이 구하는 공식 x1y1 x2y2라 하면
#(x2-x1)*(y2+y1)/2
def min(n1, n2):
    if n1>n2:
        return n2
    else:
        return n1


max = 0
l = 0
r = len(height)-1
while(l<r):
    r_ = height[r]
    l_ =  height[l]
    S = (r-l) * min(r_,l_)
    if S>max:
        max = S
    if l_>=r_:
        r -=1
    else:
        l +=1

"""
이게 되는 이유
처음에 작은걸 버리는데,  a b c d e f g h 라고 두고 a가 작다고 치자
그렇다면 길이 7에서의 값은 7a or 7h인데 지금값은 7a
이제 6에서의 제일 큰 값을 찾아야되는데 6a 6g 6b 6h이다
6a 6g는 아무 의미없다 왜냐면 더 작은게 확실하기 때문
6b 6g중 작은거 선택 b 가 작다고 치자
다음은 5a 5f 5b 5g 5c 5h인지  a f 쌍 역시 아무 의미 없고 bg 쌍도 아무 의미 없다 따라서 c h 중에 선택...
이런식으로 나가면 O(n)의 탐색으로 결과를 찾을 수 있다.
"""
print(max)