Num_of_groups = 6
names_per_group = 6

names = []
number_of_names = int(input("Please enter the number of names: "))

for i in range(number_of_names):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

groups = [[] for _ in range(Num_of_groups)]

for i in range(number_of_names):
    group_index = i // names_per_group  
    if group_index < Num_of_groups:  
        groups[group_index].append(names[i])
    else:
        print(f" There are excess names, {names[i]} could not be added.")

for i in range(Num_of_groups):
    print(f"Group {i + 1}")
    for name in groups[i]:
        print(f" {name}")
        break

