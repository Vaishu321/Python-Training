def max_values(dict):
    max = 0
    for v in dict.values():
        if v>max :
            max=v
    result=[]
    for k,v in dict.items():
        if v==max:
            result.append(k)
    print(result)

dict={"A": 85, "B": 92, "C": 78, "D": 92}
max_values(dict)
