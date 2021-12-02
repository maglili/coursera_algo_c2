from tqdm import tqdm

# Opening file
arr = []
path = "./algo1-programming_prob-2sum.txt"  # "test3.txt"
with open(path, "r") as f:
    for row in f:
        arr.append(int(row))

hash_table = {}
for num in arr:
    if num not in hash_table:
        hash_table[num] = True


# main loop
counter = 0
for target in tqdm(range(-10000, 10000 + 1)):
    for num in arr:
        if (target - num) in hash_table:
            if num != (target - num):
                counter += 1
                break

print("counter:", counter)
