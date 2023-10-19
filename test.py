'''
my_tuple = ('sara', 6, 5, 0.97)
'''

# my_tuple = ('sara', 6, 5, 0.97)

# lst = list(my_tuple)

# res = lst[0] = 'jhon'

# my_tuple = tuple(lst)

# print(my_tuple)


# for i in range(1,10):
#     if i ==5:
#         pass
#     print(i)

# pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
# for p in pat:
#    pass
#    if (p == 0):
#        current = p
#        break
#    elif (p % 2 == 0):
#        continue
#    print(p)    
# # print(current)



# n = 6  # Number of rows

# for i in range(1, n + 1):
#     # Print spaces before the numbers
#     for j in range(n - i):
#         print(" ", end=" ")
    
#     # Print the numbers and spaces
#     for k in range(i):
#         if k == 0:
#             print(i, end=" ")
#         else:
#             print(i, end=" ")
#         print(" ", end=" ")
    
#     # Move to the next line
#     print()


''' 

'''
# Bubble Sort
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
# arr = [8,6,7,4,5,1,3,2,9]
# res = bubble_sort(arr)
# print(res)

# selection sort
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i],arr[min_index] = arr[min_index],arr[i]
#     return arr
# arr = [8,6,7,4,5,1,3,2,9]
# res = selection_sort(arr)
# print(res)

# insertion sort
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         key = arr[i]
#         j = i-1
#         while j >=0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j = j-1
#         arr[j+1] = key
#     return arr
# arr = [8,6,7,4,5,1,3,2,9]
# res = selection_sort(arr)
# print(res)


################################################################################
import re


total_count = 0
miss_graduation = 0

def generate_combinations(n, slots):
    global total_count
    global miss_graduation
    stack = [(0, [])]

    while stack:
        index, current_combination = stack.pop()

        if index == n:
            cur_comb = ''.join(current_combination)
            pattern = re.compile(r'A{4,}')
            if not bool(pattern.search(cur_comb)):
                total_count += 1
                if not bool(pattern.search(cur_comb)) and cur_comb[-1] == 'A':
                    miss_graduation += 1
        else:
            for slot in slots:
                new_combination = current_combination + [slot]
                stack.append((index + 1, new_combination))

    print(f"{miss_graduation}/{total_count}")

days = int(input("Enter number of days:"))
slots = ['P', 'A']
generate_combinations(days, slots)