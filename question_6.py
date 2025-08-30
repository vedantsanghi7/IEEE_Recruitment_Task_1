cutoff_list = [
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 239),
    ("Pilani", "Eco", 271),
    ("Pilani", "Bio", 211),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 217),
    ("Goa", "Eco", 256),
    ("Goa", "Bio", 204),
    ("Hyderabad", "CS", 295),
    ("Hyderabad", "Chemical", 216),
    ("Hyderabad", "Eco", 251),
    ("Hyderabad", "Bio", 203),
]

cutoff_dict = {}
for campus, branch, score in cutoff_list:
    if campus not in cutoff_dict:
        cutoff_dict[campus] = {}
    cutoff_dict[campus][branch] = score

print("Original List")
for item in cutoff_list:
    print(item)
    
print("\nConverted Dictionary")
print(cutoff_dict)

