
import random

random.seed('class_03_random_seed')
BIN_SIZE = 40
nums = [ random.randint(2, 9) for _ in range(20) ]
print(nums)

#bin = [ 1, 2, 3 ]
#bins = [ bin ]

def bin_free(bin):
    return BIN_SIZE - sum(bin)

def bin_can_hold(bin, size):
    return bin_free(bin) >= size

def new_bin():
    nb = []
    bins.append(nb)
    return nb

def first_fit(size):
    for b in bins:
        if bin_can_hold(b, size):
            return b
    return new_bin()

def next_fit(size):
    global last_bin
    if last_bin and bin_can_hold(last_bin, size):
        return last_bin
    return new_bin()


def best_fit(size):
    smallest_bin = None
    smallest_space = BIN_SIZE
    for b in bins:
        space = bin_free(b)
        if space >= size and space < smallest_space:
            smallest_bin = b
            smallest_space = space
    return smallest_bin if smallest_bin else new_bin()

def worst_fit(size):
    largest_bin = None
    largest_space = 0
    for b in bins:
        space = bin_free(b)
        if space >= size and space > largest_space:
            largest_bin = b
            largest_space = space
    return largest_bin if largest_bin else new_bin()

strategies = {"first_fit": first_fit, "next_fit": next_fit, "best_fit": best_fit, "worst_fit": worst_fit}

for name, strategy in strategies.items():
    print(f"\nFunction: <<{name}>>")
    bins = []
    last_bin = None
    for num in nums:
        bin = strategy(num)
        bin.append(num)
        last_bin = bin
    print(bins)
