def sets_are_disjoint(set1, set2):
    if set1&set2==0:
        print("Sets are disjoint")
    else:
        print("Sets are not disjoint")

set1={1,2,3,4,5,6,7,8,9}
set2={1,2,3,4,5,6,7,8,9}
sets_are_disjoint(set1, set2)
