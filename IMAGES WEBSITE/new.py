
# list1 = [10, 5, 4]

# print(list1)

# list2 = list1.sort()

# print("Largest element is:", list1[-1])

# list1[-1] = list1[-1] - 1
# print(list1)



# def max_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a-1
            
#     return max
# print(max_num_in_list([1,5, 4]))



# h = [1,50,40]
# largest_number = h[0]
# for number in h:
#     if number > largest_number:
#         largest_number = number
# print(largest_number)



# largest_number = largest_number-1
# print(largest_number)


# h = list(map(lambda x: x.replace('largest_number', 'largest_number'), h))

h=[1,50,40]
maxValue = max(h)
print(maxValue)

a = h.index(maxValue)
h[a] = maxValue-1


print(h)