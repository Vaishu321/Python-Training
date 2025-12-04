def present_union_not_in_intersection(set1, set2):
    union_set = (set1|set2)
    intersection_set = (set1&set2)
    elements_set = union_set-intersection_set
    print(elements_set)

set1={1,2,3,4}
set2={4,5,6,7,8}
present_union_not_in_intersection(set1, set2)
