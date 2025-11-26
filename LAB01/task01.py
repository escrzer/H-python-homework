def get_numbers_from_user():
    num_in = []
    while len(num_in) < 10:
        user_input = input('Введите целое число: ')
        try:
            num = int(user_input)
            num_in.append(num)
        except ValueError:
            print('Это не целое число, попробуйте снова.')
    return num_in


def find_min(num_min):
    minimum = num_min[0]
    for num in num_min[1:]:
        if num < minimum:
            minimum = num
    return minimum


def find_max(num_max):
    maximum = num_max[0]
    for num in num_max[1:]:
        if num > maximum:
            maximum = num
    return maximum


def sum_numbers(nums):
    summ = 0
    for num in nums:
        summ += num
    return summ


if __name__ == '__main__':
    numbers = get_numbers_from_user()
    print(find_min(numbers))
    print(find_max(numbers))
    print(sum_numbers(numbers))#!/usr/env/python

