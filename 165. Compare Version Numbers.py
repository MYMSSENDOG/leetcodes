class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = []
        v2 = []
        v1 += (int(i) for i in version1.split("."))
        v2 += (int(i) for i in version2.split("."))
        m = min(len(v1), len(v2))
        for i in range(m):
            if v1[i] == v2[i]:
                continue
            elif v1[i] > v2[i]:
                return 1
            else:
                return -1
        if sum(v1[m:])>sum(v2[m:]):
            return 1
        elif sum(v1[m:])==sum(v2[m:]):
            return 0
        else:
            return -1

sol = Solution()
version1 = "1"
version2 = "1"
print(sol.compareVersion(version1, version2))