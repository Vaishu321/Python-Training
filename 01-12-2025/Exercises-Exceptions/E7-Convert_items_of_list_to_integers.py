# Write a program that attempts to convert items of a list to integers, handling conversion errors individually.

def convert_items_of_list_to_integers(list):
    list1 = []
    for item in list:
        try:
            item=float(item)
            item=int(item)
            list1.append(item)
        except ValueError:
            print("Invalid Conversion")
    print(list1)

convert_items_of_list_to_integers([1,2.2,"How","3.2",4])
