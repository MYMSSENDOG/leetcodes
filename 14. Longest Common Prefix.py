input = ["dog", "car", "flight"]
prefix = input[0]
max_length = len(input[0])
if prefix == "":
    print("")
for s in input[1:]:



    for i, c in enumerate(s):
        if prefix == "":
            print(prefix)
            break
        if c == prefix[i]:
            pass
        else:
            max_length = i
            prefix = prefix[:max_length]
            break
print(prefix)