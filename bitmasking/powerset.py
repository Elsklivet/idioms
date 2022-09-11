# Get the powerset (all combinations)
# of a list by using bitmasking. 
# Optionally provide an 'r' value and filter out only
# subsets of that length.
def powerset(l, r=None):
    subsets = []
    length = len(l)
    
    for check in range(0, 1 << length):
        this_subset = []
        for index, item in enumerate(l):
            if ((1 << index) & check) != 0:
                this_subset.append(item)
        subsets.append(this_subset)
    if r:
        actual = []
        for subset in subsets:
            if len(subset) == r:
                actual.append(subset)
        return actual
    else:
        return subsets