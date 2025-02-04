from itertools import count


# def geometric_progression(a_1, b , max_terms):
#     quantity = 0
#     raise
#     while quantity < max_terms:
#         yield a_1
#         a_1 *= b
#         quantity += 1
#
# a_1 = 3
# b = 5
# max_terms = 7 # килькисть геометричної прогресії
#
# res = geometric_progression(a_1, b , max_terms)
# for terms in res:
#     print(terms)
#
#                  1(2)
#
# def geometric_progression(a_1, b , max_terms):
#     if not isinstance(a_1, (int | float)):
#         raise TypeError('a_1 повіно буди цілим числом або с плавающой комой')
#     if not isinstance(b, (int | float)):
#         raise TypeError('b повіно буди цілим числом або с плавающой комой')
#     if not isinstance(max_terms, int):
#         raise TypeError ('max_terms повинно бути чілим числом')
#     if max_terms <= 0:
#         raise ValueError('max_terms повинно буди більше нуля')
#
#     quantity = 0
#     while quantity < max_terms:
#         yield a_1
#         a_1 *= b
#         quantity += 1
#
# a_1 = 3
# b = 5
# max_terms = -7 # килькисть геометричної прогресії
#
# res = geometric_progression(a_1, b , max_terms)
# for terms in res:
#     print(terms)
#
# try:
#     res = geometric_progression(a_1, b, max_terms)
#     for terms in res:
#         print(terms)
#
# except Exception as x:
#     print(x)



                   #5

# from datetime import datetime, timedelta
#
# def date_generator(start_date, end_date, step_days):
#     current_date = start_date
#     while current_date <= end_date:
#         yield current_date
#         current_date += timedelta(days=step_days)
#
## задаємо початкову і кінцеву дату
# start_date = datetime(2025, 2, 3)
# end_date = datetime(2025, 2, 25)
# step_days = 2  #крок між днями
#
# for date in date_generator(start_date, end_date, step_days):
#     print(date.strftime('%Y-%m-%d'))

                           #5(1)

# from datetime import datetime
# from dateutil.relativedelta import relativedelta #в командній строкі загрузить "pip install python-dateutil"
#
# def date_generator(start_date, end_date, step_months):
#     current_date = start_date
#     while current_date <= end_date:
#         yield current_date
#         current_date += relativedelta(months=step_months)
#
# # задаємо початкову і кінцеву дату
# start_date = datetime(2025, 2, 3)
# end_date = datetime(2025, 12, 25)
# step_months = 2 # крок між місяцями
#
# for date in date_generator(start_date, end_date, step_months):
#     print(date.strftime('%Y-%m-%d'))

#------------------------------------------------------------------------



                           # 1

def my_decorator(func):
    def wrapper(value):
        print(f'Поточне значення: {value}')
        return func(value)
    return wrapper

@my_decorator
def user_function(x):
    return x + 2


def sequence_generator(user_function, start_value, n, stop_value):
    value = start_value
    count = 0

    while count < n:
        yield value
        value = user_function(value)
        count += 1
        if value > stop_value:
            break

def user_function(x):
    return x + 2

gen = sequence_generator(user_function, start_value=0, n=9, stop_value=18)

for num in gen:
    print(num)

                              #3


def function_sum(numbers, user_function):
    trans_numbers = [user_function(num) for num in numbers]
    return trans_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
user_function = lambda x: x ** 2
res = function_sum(numbers, user_function)
print(res)