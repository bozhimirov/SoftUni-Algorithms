def rev_array(idx, elem):
    if idx == len(elem) // 2:
        return
    swap_idx = len(elem) - 1 - idx
    elem[idx], elem[swap_idx] = elem[swap_idx], elem[idx]
    rev_array(idx + 1, elem)


elem = input().split()

rev_array(0, elem)
print(' '.join(elem))
