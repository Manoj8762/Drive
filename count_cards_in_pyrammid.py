# lavel 1 2 cards=2
# level 2 cards=7
# level 3 cards=15
# cards_at_current_level=2*current_level+current_level-1 + cards at previous level

def level(n):
    if n == 0:
        return 0
    if n == 1:
        return 2

    card = [0] * (n + 1)
    print(card)
    card[1] = 2

    for i in range(2, n + 1):
        card[i] = (2 * i + (i - 1) + card[i - 1]) % 1000007

    return card[1:]   # returns number of cards at level n
print(level(4))
