import time
from linked_list import LinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for n in names_1:
    if n in names_2:
        duplicates.append(n)

# duplicates = LinkedList()
# for i in range(len(names_1)):
#     if names_1[i] in names_2:
#         duplicates.add_to_head(names_1[i])
        
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# runtime complexity for given code is 0(n^2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")

# next_name = duplicates.head
# while next_name != None:
#     print(next_name.value)
#     next_name = next_name.next_node

print (f"runtime: {end_time - start_time} seconds")
