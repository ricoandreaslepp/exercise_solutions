file = open("jagasis.txt", "r")
output = open("jagaval.txt", "w")

n = int(file.readline())
numbers = []

total_sum = 0
for _ in range(0, n):
    current = int(file.readline())
    numbers.append(current)
    total_sum += current
    

min_distance = 1000000
current_sum = 0
ans = 0
for i in range(0, n):
    current_sum += numbers[i]
    if (abs(current_sum - (total_sum - current_sum)) < min_distance):
        min_distance = abs(current_sum - (total_sum - current_sum))
        ans = i+1

output.write(str(ans))
output.close()
