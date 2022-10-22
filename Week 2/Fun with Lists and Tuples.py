# Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

list_of_tuples = [(5, 7), (12, 74), (20, 13), (45, 2), (23,6)]

# Sorting List of Tuples in Increasing order by last element 
for i in range(1, len(list_of_tuples)):
    for j in range(len(list_of_tuples) - i):
        if(list_of_tuples [j][1] > list_of_tuples [j+1][1]):
            temp = list_of_tuples [j]
            list_of_tuples [j] = list_of_tuples[j + 1]
            list_of_tuples [j + 1] = temp

print('Sorted List : ' + str(list_of_tuples))