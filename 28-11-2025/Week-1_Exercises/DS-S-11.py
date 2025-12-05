
def elements_with_freq_two(lst):
    seen_once = set()
    seen_twice = set()
    seen_more = set()

    for x in lst:
        if x in seen_more:
            continue
        elif x in seen_twice:
            # third time — no longer exactly twice
            seen_twice.remove(x)
            seen_more.add(x)
        elif x in seen_once:
            # second time
            seen_once.remove(x)
            seen_twice.add(x)
        else:
            # first time
            seen_once.add(x)

    return seen_twice

data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(elements_with_freq_two(data))
