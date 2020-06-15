# this is a combination of lambda and map

new_Map = map(lambda num: num%2, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# this applies to all the number and prints the numbers, it doesnt use the concept of predicates
for numbers in new_Map:
    print("Modules of the number are : ", numbers)

# filters use the concept of predicates
new_filter = filter(lambda filtered_collection: filtered_collection % 2 == 0, [1, 2, 3, 45, 6, 7, 8, 9, 10, 11, 12])

for filtered_col in new_filter:
    print("Filtered collection : ", filtered_col)

