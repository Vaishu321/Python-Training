
def merge_dicts_always_list(d1, d2):
    merged = {}
    for k, v in d1.items():
        merged.setdefault(k, []).append(v)
    for k, v in d2.items():
        merged.setdefault(k, []).append(v)
    return merged
