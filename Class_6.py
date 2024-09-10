#1 You have given a python list [10,501,22,37,100,999,87,351] your task is to craete two List one which have all the even Numbers and another List which will have all the ODD numbers in it?

def list_number(list):
    even_number = []
    odd_number = []

    for i in list:
        if i%2==0:
            even_number.append(i)
        else:
            odd_number.append(i)

    return even_number,odd_number

list= [10,501,22,37,100,999,87,351]
even_number,odd_number=list_number(list)
print(even_number)
print(odd_number)

#2 Given a Python list [10,501,22,37,100,999,87,351] your task is to count all the Prime Numbers and create a new Python List which will count all the Prime Numbers in it

def Prime_number(list):
    New_list=[]

    for i in list:
        if i>1:
            for j in range(2,int(i**0.5)+1):
                if i % j==0:
                    break
            else:
                New_list.append(i)

    return New_list

list=[10,501,22,37,100,999,87,351]
New_list= Prime_number(list)
print(New_list)

#3 Given a Python list [10,501,22,37,100,999,87,351] Find out how many numbers are there in the given Python List which are Happy Numbers?

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1

def find_happy_numbers(numbers):
    happy_numbers = []


    for number in numbers:
        if is_happy(number):
            happy_numbers.append(number)

    return happy_numbers

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = find_happy_numbers(numbers)
happy_count = len(happy_numbers)

print("Happy numbers:", happy_numbers)
print("Count of happy numbers:", happy_count)

#4 Write a python program to find the sum of the first and last digit of an integer

def sum_first_last_digit(number):
    num_str = str(number)

    first_digit = int(num_str[0])
    last_digit =  int(num_str[-1])

    return first_digit + last_digit

number= 121
result= sum_first_last_digit(number)
print(f"The sum of first and last dist of {number} is : {result}")

#5 You have given  a list of N integers  which represents the numbers of mangoes in bag .Each bag has variable number of mangoes.
#There are M students ina Guvi class, your task is to distribute the mangoes in sucha way that each student get one bag. The difference between the number of
#mangoes in a bag with maximum mangoes and bag with minimum mangoes given to the student is minimum?


def min_mango_difference(mangoes, M):
    mangoes.sort()

    min_diff = float('inf')

    for i in range(len(mangoes) - M + 1):
        current_diff = mangoes[i + M - 1] - mangoes[i]

        if current_diff < min_diff:
            min_diff = current_diff

    return min_diff


mangoes = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43]
M = 7
min_difference = min_mango_difference(mangoes, M)
print("The minimum difference is:", min_difference)

#6 You have a given  three list. Your task is to find the duplicates in the three lists.Write a python program for the same.You can use your own python list.

def duplicates(list1, list2, list3):
    set1= set(list1)
    set2= set(list2)
    set3= set(list3)

    duplicate_numbers = set1.intersection(set2,set3)
    return duplicate_numbers

list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]
list3 = [3,4,5,6,7]

result= duplicates(list1,list2,list3)
print(f"The duplicate in all 3 list are {result}")

#7 Write a python program to find the first non repeating element in the given list of integers.

def non_repeating_element(number_list):
    frequency= {}

    for num in number_list:
       if num in frequency:
        frequency[num] = frequency[num]+1
       else:
           frequency[num] = 1

    for num in frequency:
        if frequency[num] == 1:
            return num

    return print("All number are repeating")

number_list = [1,1,2,2,3,3,4,4,5,6,7]
first_non_repeating_number = non_repeating_element(number_list)
print(f"The first non repeating number in the list is: {first_non_repeating_number}")

#8 Write a python program to find the minimum element in a rated and sorted list?

def minimum_element(numbers_ist):

    min_number = numbers_ist[0]

    for num in number_list:
        if num < min_number:
            min_number = num

    return min_number

number_list = [8,7,6,5,0,4,3,2,1]
minimum_element_in_list = minimum_element(number_list)
print(f'The minimum element in the list is:{minimum_element_in_list}')

#9 You have been givan a python list[10,20,30,9] and a value of 59 Write a python program to find the triplet in the list whose sum is equal to the given value?


def tripet_sum(numbers_list, value):

    for i in range(0,len(numbers_list)):
        for j in range (i+1,len(numbers_list)):
            for k in range (j+1,len(numbers_list)):
                if numbers_list[i] + numbers_list[j] + numbers_list[k] == value:
                    return numbers_list[i],numbers_list[j],numbers_list[k]

    return print("No numbers sum is 59")

numbers_list = [10,20,30,9]
value= 59
triplet_found = tripet_sum(numbers_list,value)
print(f'The numbers from list whose sum is 59:{triplet_found}')


#10 Given a list[4,2,-3,1,6] Write a python program to find if there is a sublist with sum equal to zero?


def sublist(numbers_list):

    for i in range(0,len(numbers_list)):
        for j in range(i+1,len(numbers_list)):
            for k in range(j+1,len(numbers_list)):
                if numbers_list[i] + numbers_list[j] + numbers_list[k] == 0:
                    return numbers_list[i], numbers_list[j], numbers_list[k]

    return None

numbers_list = [4,2,-3,1,6]
sublist_with_sum_zero = sublist(numbers_list)
print(f"The sublist with sum equal to zero:{sublist_with_sum_zero}")