#creating empty list
my_list=[]
#appending 10,20,30,40 to my empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#inserting value 15 at the second position
my_list.insert(1,15)
#creating a new list
list2 = [50,60,70]
# Extending my_list with the new list
my_list.extend(list2)
#Removing the last element from my_list
my_list.pop()
# sort my_list in ascending order
my_list.sort(reverse=False)
# print the index of the value 30 in my_list
print(my_list.index(30))