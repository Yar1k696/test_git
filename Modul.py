#                      # Task 5
#
# def log_arguments_results(func):
#     def wrapper(*args, **kwargs):
#         print(f'arguments: {args}, {kwargs}')
#         res = func(*args, **kwargs)
#         print(f'result: {res}')
#         return res
#     return wrapper
#
# @log_arguments_results
# def add_numbers(a, b):
#     return a + b
#
# add_numbers(3, 4)
#
# def before_and_after(func):
#     def wrapper(*args, **kwargs):
#         print('executing before the function')
#         result = func(*args, **kwargs)
#         print('executing after the function')
#         return result
#     return wrapper
#
# @before_and_after
# def some_funs():
#     print('function call')
#
# some_funs()
