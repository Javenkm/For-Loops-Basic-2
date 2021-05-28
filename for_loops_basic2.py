# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 2, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5].
def biggieSize(list):
    for x in range(0, len(list), 1):
        if(list[x] > 0):
            list[x] = "big"
    return list
print(biggieSize([-1, 3, 5, -5]))

# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered be a positive number)
# Example: count_positives([-1, 1, 1, 1]) changes the original list to [-1, 1, 1, 3] and returns it
# Example: count_positives([1, 6, -4, -2, -7, -2]) changes the list ot [1, 6, -4, -3, -7, 2].
def countPos(list):
    count = 0
    for x in range(0, len(list), 1):
        if(list[x] > 0):
            count += 1
    list[len(list) - 1] = count
    return list
print(countPos([1, 3, -2, 7, -2, 5]))

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1, 2, 3, 4]) should return 10
# Example: sum_total([6, 3, -2]) should return 7.
def sumTotal(list):
    sum = 0
    for x in range(0, len(list), 1):
        sum = sum + list[x]
    return sum
print(sumTotal([4, 3, 5, 2, 6, 1]))
print(sumTotal([1, 2, 3, 4]))
print(sumTotal([6, 3, -2]))

# 4. Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1, 2, 3, 4]) should return 2.5
def average(list):
    sum = 0
    for x in range(0, len(list), 1):
        sum = sum + list[x]
    avg = sum / len(list)
    return avg
print(average([4, 3, 2, 1]))
print(average([1, 2, 3, 4, 5, 6, 7]))

# 5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37, 2, 1, -9]) should return 4.
# Example: length([]) should return 0.
def length(list):
    count = 0
    for x in range(0, len(list), 1):
        count += 1
    return count
print(length([]))
print(length([37, 2, 1, -9]))
print(length([1, 2, 3, 4, 5, 6]))

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37, 2, 1, -9]) should return -9.
# Example: minimum([]) should return False.
def minimum(list):
    if(len(list) < 1):
        return False
    min = list[0]
    for x in range(0, len(list), 1):
        if (list[x] < min):
            min = list[x]
    return min
print(minimum([3, 2, 1, 4, 5, 6]))
print(minimum([]))
print(minimum([37, 2, 1, -9]))

# 7. Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37, 2, 1, -9])) should return 37
# Example: maximum([]) should return False.
def maximum(list):
    if(len(list) < 1):
        return False
    max = list[0]
    for x in range(0, len(list), 1):
        if (list[x] > max):
            max = list[x]
    return max
print(maximum([1, 2, 3, 4, 5, 6, 7, 89, 99]))
print(maximum([1, 2, 3, 4, 5]))
print(maximum([37, 2, 1, -9]))
print(maximum([]))

# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum, and length of the list.
# Example: ultimate_analysis([37, 2, 1, -9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4}
def ultimateAnalysis(list):
    sum = 0
    min = list[0]
    max = list[0]
    length = len(list)
    for x in range(0, len(list), 1):
        sum = sum + list[x]
        if(list[x] < min):
            min = list[x]
        if(list[x] > max):
            max = list[x]
    avg = sum / length
    dictionary = {
        'sumTotal': sum,
        'average': avg,
        'minimum': min, 
        'maximum': max, 
        'length': length
    }
    return dictionary
print(ultimateAnalysis([37, 2, 1, -9]))

# 9. Reverse List - Create a function that takes a list and returns that list with values reversed. Do this without creating a second list. (This challenge is know to appear during basic technical interviews).
# Example: reverse_list([37, 2, 1, -9]) should return [-9, 1, 2, 37].
def reverseList(list):
    for x in range(0, len(list)//2, 1):
        temp = list[x]
        list[x] = list[len(list) - 1 - x]
        list[len(list) - 1 - x] = temp
    return list
print(reverseList([37, 2, 1, -9]))
print(reverseList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))