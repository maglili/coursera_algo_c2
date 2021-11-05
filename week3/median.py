import heapq

# Input files
path = "./Median.txt"
# ath = "./test2.txt"
nums = []
with open(path, "r") as f:
    for row in f:
        nums.append(int(row))

# min / max heap
h_low = []  # half-lower values, max heap
h_high = []  # half-larger values, min heap
lower_frag = False
high_frag = False
counter = 1
median_sum = 0

for num in nums:
    # initial condition
    if h_low == []:
        h_low.append(-1 * num)
        heapq.heapify(h_low)
        lower_frag = True

    else:
        # num > max of h_low
        if num > -1 * h_low[0]:
            if h_high == []:
                h_high.append(num)
                heapq.heapify(h_high)
                high_frag = True
            else:
                if not high_frag:
                    heapq.heappush(h_high, num)
                    high_frag = True
                else:
                    heapq.heappush(h_high, num)

                    h_min = heapq.heappop(h_high)
                    heapq.heappush(h_low, -1 * h_min)
                    high_frag = False

        # num <= max of h_low
        else:
            if not lower_frag:
                heapq.heappush(h_low, -1 * num)
                lower_frag = True
            else:
                heapq.heappush(h_low, -1 * num)

                l_max = -1 * heapq.heappop(h_low)
                heapq.heappush(h_high, l_max)
                lower_frag = False

    if len(h_low) < len(h_high):
        median_sum += h_high[0]
    else:
        median_sum += -1 * h_low[0]

    counter += 1
    # print(h_low)
    # print(h_high)
    # print(median_sum)
    # print("=" * 20)

print("ans:", median_sum % 10000)
print(len(h_low))
print(len(h_high))
