class Solution:
    def LowestDamage(self, monsters):
        damage = 0
        mon_damage = 0
        priority = []
        for i, m in enumerate(monsters):
            hp, ap = m
            mon_damage += ap
            priority.append([ap / hp, hp])
        priority.sort()
        damage -=mon_damage * priority[0][1]
        for p, h in priority:
            damage += mon_damage * h
            mon_damage -= p * h
        return damage


sol = Solution()
monsters = [[i,i] for i in range(1,11)]
print(sol.LowestDamage(monsters))