#  Python Program to convert List to Set

test_list = [[1, 2, 1], [1, 2, 3], [2, 2, 2, 2], [0]]

print("The original list of lists : " + str(test_list))
 

res = [set(ele) for ele in test_list]
 
# print result
print("The converted list of sets : " + str(res))