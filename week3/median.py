import heapq

# Input files
path = "./Median.txt"
nums = []
with open(path, "r") as f:
    for row in f:
        nums.append(int(row))

# min / max heap
h_low = []  # half - lower values, max heap
h_high = []  # half - larger values, min heap
add_counter = 0

for num in nums:
    # initial condition
    if h_low == []:
        h_low.append(-1 * num)
        heapq.heapify(h_low)
        continue

    # num > max of h_low
    if num > -1 * h_low[0]:
        if h_high == []:
            h_high.append(num)
            heapq.heapify(h_high)
        else:
            heapq.heappush(h_high, num)

    # num <= max of h_low
    else:
        if add_counter < 1:
            heapq.heappush(h_low, -1 * num)
            add_counter += 1
        else:
            l_max = -1 * heapq.heappop(h_low)
            heapq.heappush(h_high, l_max)
            heapq.heappush(h_low, -1 * num)
            add_counter = 0

print(len(h_low))
print(len(h_high))
