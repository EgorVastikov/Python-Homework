nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
result_list = [number for sublist1 in nice_list for sublist2 in sublist1 for number in sublist2]
print(result_list)