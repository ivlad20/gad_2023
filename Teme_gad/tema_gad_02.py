mylist = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

mylist_sorted_asc = sorted(mylist)
mylist_sorted_desc = sorted(mylist, reverse = True)

print(f"Lista ordonata ascendent este: {mylist_sorted_asc}")
print(f"Lista ordonata descendent este: {mylist_sorted_desc}")

print(f"Elementele pare din lista sunt: {mylist_sorted_asc[1::2]}")
print(f"Elementele impare din lista sunt: {mylist_sorted_asc[::2]}")

print(f"Elementele din lista care sunt multiplii de 3 sunt: {mylist_sorted_asc[2::3]}")