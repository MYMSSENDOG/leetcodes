def print_cards(cards):
    ret = ""
    for c in cards:
        ret += c + " "
    print(ret.rstrip())

user_input = input().split()
cards = [card for card in user_input]
last = []
for i, c in enumerate(cards):
    if c in last:
        last.pop(last.index(c))
    if len(last) >= 5:
        last.pop()
    last.insert(0, c)
    print_cards(last)



