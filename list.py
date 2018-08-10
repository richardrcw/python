list1 = [1,2,3]
list2 = list("hello world")
list3 = list(list2)
list4 = list3
print("list1: {}\nlist2: {}\nlist3: {}".format(list1, list2, list3))
print("list2 == list3: {}".format(list2 == list3))
print("list3 is list4: {}".format(list3 is list4))
