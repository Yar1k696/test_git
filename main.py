#                          # Task 3
#
# def handle_exceptions(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             print(f'An error occurred {e}')
#             return None
#     return wrapper
#
# @handle_exceptions
# def divide(a, b):
#     return a / b
#
# result = divide(5, 0)
# print(result)
#
#
#                         # Task 4
#
# import time
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f'execution time: {execution_time:.5f} second')
#         return result
#     return wrapper
#
#
#
# @measure_time
# def some_function():
#     time.sleep(2)
#
# some_function()
#
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


