path = "./Median.txt"
nums = []
with open(path, "r") as f:
    for row in f:
        nums.append(int(row))

min_h = []
max_h = []
