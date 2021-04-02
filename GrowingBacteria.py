# target = 47
target = 1000000000000

day1, day2, day3, day4 = 1, 0, 0, 0
generation = 1

while(day1 + day2 + day3 + day4 < target):
    generation += 1
    day1, day2, day3, day4 = day1 + day2, day1, day2, day3
    # print(day1, day2, day3, day4)

print(generation)
