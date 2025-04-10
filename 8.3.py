max_weight = int(input())
fishmen = int(input())
fishmen_weights = list(map(int, input().split()))
lodka = []
count_fishmen = 0


for i in range(len(fishmen_weights)):
    if fishmen_weights[i] <= max_weight:
        lodka.append(fishmen_weights[i])

        if len(lodka) == 2:
            if lodka[0] + lodka[1] > max_weight and lodka[0] > lodka[1]:
                count_fishmen += 1
                del lodka[0]
            if lodka[0] + lodka[1] > max_weight and lodka[1] > lodka[0]:
                count_fishmen += 1
                del lodka[1]
        if len(lodka) == 2:
            count_fishmen += 1
            lodka.clear()

if len(lodka) > 0:
    count_fishmen += 1
    lodka.clear()

print(count_fishmen)