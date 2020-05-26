inv_map = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

def number_to_pattern(index, k):
    if k == 1:
        return inv_map[index]
    pattern_collect = ''
    while index != 0:
        pattern_collect = inv_map[index % 4] + pattern_collect
        index = index // 4
        number_to_pattern (index, k)
    if len(pattern_collect) < k:
        pattern_collect =  (k - len(pattern_collect))*'A' + pattern_collect
        return pattern_collect

print number_to_pattern(6625,10)