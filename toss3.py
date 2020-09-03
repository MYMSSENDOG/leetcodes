
# [!!주의!!] compute 함수는 이미 구현되어있지만, 숨김처리되어 있습니다. 호출해서 테스트 해주세요.
user_input = input().split()
nums = [int(i) for i in user_input]
memo = {}
ret = ""
for n in nums:
	if n in memo:
		ret += str(memo[n]) + " "
	else:
		t = compute(n)
		ret += str(t)
		memo[n] = t
print(ret.rstrip())
