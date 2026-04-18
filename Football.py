from collections import Counter
teams = []
for _ in range(int(input())):

    s = input()
    teams.append(s)

teams = Counter(teams)

print(teams.most_common()[0][0])
