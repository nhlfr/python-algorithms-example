def partition(lst, begin, end):
    i = begin - 1
    for j in xrange(begin, end):
        if lst[j] < lst[end]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[end] < lst[i + 1]:
        lst[i + 1], lst[end] = lst[end], lst[i + 1]
    return i + 1


def _qsort(lst, begin, end):
    if begin < end:
        p = partition(lst, begin, end)
        _qsort(lst, begin, p - 1)
        _qsort(lst, p + 1, end)


def qsort(lst):
        _qsort(lst, 0, len(lst) - 1)
