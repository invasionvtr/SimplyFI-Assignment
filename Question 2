def min_players_to_shot(n, k, heights):
    line_of_sight = max(n, k)
    max_height = 0
    count = 0
    for h in heights:
        if h > max_height:
            max_height = h
        if max_height > line_of_sight:
            count += 1
            max_height = h
    return count
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    print(min_players_to_shot(n, k, heights))
