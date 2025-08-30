list1 = [3, 4, 5, 1, 4, 6, 1, 7, 7]
list2 = [5, 8, 2, 9, 9, 4, 6, 3]

set1 = set(list1)
set2 = set(list2)
intersection_set = set1 & set2
# Sets remove duplicates and the '&' operator finds the intersection

final_list = list(intersection_set)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"\nIntersection of the two lists: {final_list}")

