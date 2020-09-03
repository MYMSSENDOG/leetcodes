# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input().split()
lottery = [int(i) for i in user_input]

if len(lottery) != 6:
    print(False)
elif sorted(lottery) != lottery:
    print(False)
elif not (1 <= lottery[0] <= 45) or not (1 <= lottery[-1] <= 45):
    print(False)
print(True)

