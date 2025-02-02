
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
#
#                       3
#
#
def alternative_range(start, stop=None, step=1):
    if stop is None:
        stop = start
    start = 0
    current = start
    while current < stop:
        yield current
        current += step

for num in alternative_range(1, 30, 2):
    print(num)